import json
import glob
import pickle
import os
import random
import hashlib
import uuid
import datetime
from typing import List, Dict

import flask
import numpy as np

import function.structure.data
from function.reader.exceptions import ReaderWrongException
from function.structure.exceptions import TDSEmptyException
from function.exceptions import TanswerSIDException

if not os.path.isdir("./dataset"):
    os.mkdir("./dataset")
if not os.path.isdir("./preference"):
    os.mkdir("./preference")

app = flask.Flask("tanswer")

### config
if not os.path.isfile("./config.json"):
    with open("./config.json", 'w', encoding='utf-8') as f:
        json.dump({"host": "127.0.0.1", "port": "5000", "debug": False,
                   "filesize": 32, "session_lifetime": 10},
                  f,
                  indent=4)

with open("./config.json", 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)

app.config["MAX_CONTENT_LENGTH"] = int(CONFIG["filesize"] * 1024 * 1024)
app.jinja_env.globals.update(
    zip=zip, enumerate=enumerate, len=len
)

app.secret_key = hashlib.sha256(f"{random.uniform(0, 1 << 12)}".encode('utf-8')).digest()

# temporary use this variable to save

db_LAST: Dict[str, datetime.datetime] = dict()
db_TDS: Dict[str, function.structure.data.TanswerDataStruct] = dict()
db_SAMPLE: Dict[str, list] = dict()
db_W: Dict[str, np.ndarray] = dict()
db_W_name: Dict[str, str] = dict()


@app.before_request
def session_check():
    flask.session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=CONFIG["session_lifetime"])
    if "id" not in flask.session:
        sid = flask.session["id"] = str(uuid.uuid4())
        db_TDS[sid] = None
        db_SAMPLE[sid] = None
        db_W[sid] = None
        db_W_name[sid] = "W.pkl"
        db_LAST[sid] = datetime.datetime.now()


@app.errorhandler(413)
def file_size_error(error):
    return "file size is so big", 413


@app.errorhandler(TanswerSIDException)
def tanswer_sid_error(error):
    return "maybe it's been too long."


@app.route("/")
def front():
    print(flask.session.get("id"))
    return flask.render_template("front.html")


@app.route("/select/", methods=["GET"])
def select():
    files = [os.path.basename(f) for f in glob.glob(os.path.join(os.getcwd(), 'dataset', "*.tnw"))]
    return flask.render_template("select.html", files=files)


@app.route("/fast_start/", methods=["GET"])
def fast_start():
    return flask.render_template("fast_start.html")


@app.route("/compile/", methods=["POST"])
def compile():
    # code for something compile
    if "file" in flask.request.files:
        f = flask.request.files["file"]
        if f.filename == '':
            return flask.redirect(flask.url_for("ready"))
        try:
            db_TDS[flask.session.get("id")] = function.structure.data.TanswerDataStruct(f.read().decode("utf-8"), "",
                                                                                        "")
        except ReaderWrongException:
            return "reader wrong"
        except UnicodeDecodeError:
            return "not unicode text"
        except TDSEmptyException:
            return "tds empty exception"
    elif "file" in flask.request.form:
        fname = flask.request.form["file"]
        with open(os.path.join(os.getcwd(), "dataset", fname), 'r', encoding='utf-8') as f:
            try:
                db_TDS[flask.session.get("id")] = function.structure.data.TanswerDataStruct(f.read(), "", "")
            except ReaderWrongException:
                return "reader wrong"
            except UnicodeDecodeError:
                return "not unicode text"
            except TDSEmptyException:
                return "tds empty exception"
    else:
        return "invalid post"

    return flask.redirect(flask.url_for("ready"))


@app.route("/ready/", methods=["GET"])
def ready():
    warn_message = flask.request.args.get("warn_message", None)
    weights = [os.path.basename(f) for f in glob.glob(os.path.join(os.getcwd(), "preference", "weight", "*.pkl"))]
    return flask.render_template("ready.html", tds=db_TDS[flask.session.get("id")], weights=weights,
                                 warn_message=warn_message)


@app.route("/start/", methods=["POST"])
def start():
    # get weight
    weight_is_default = flask.request.form.get("weight-is-default")
    w_name = None

    sid = flask.session.get("id")
    tds = db_TDS.get(sid)

    if tds is None:
        raise TanswerSIDException

    if weight_is_default:
        try:
            weight_default_value = int(flask.request.form.get("weight-default-value"))
            if 1 <= weight_default_value <= 100:
                w = tds.make_init_weight(default=weight_default_value)
            else:
                raise Exception
        except Exception:
            w = tds.make_init_weight()
    else:
        selected_weight = flask.request.form.get("selected-weight")
        if selected_weight:
            with open(os.path.join(os.getcwd(), "preference", "weight", selected_weight), 'rb') as f:
                try:
                    w = pickle.load(f)
                except (EOFError, pickle.PickleError):
                    w = None
            w_name = selected_weight
        else:
            w = tds.make_init_weight()

    if not w_name:
        w_name = "W.pkl"

    # weight validity check
    if not tds.valid(w):
        return flask.redirect(flask.url_for("ready", warn_message="Invalid Weight Object"))

    # processing sampling
    wil = int(flask.request.form.get("wil"))
    if wil < 0:
        return flask.redirect(flask.url_for("ready", warn_message="Invalid Wil(number of repeat)"))
    selected_stages = list(map(int, flask.request.form.getlist("selected-stages")))

    db_W[sid] = w
    db_W_name[sid] = w_name
    s = db_SAMPLE[sid] = tds.sampling(wil, w, stages=selected_stages)
    return flask.render_template("start.html", samples=s)


@app.route("/get/samples/")
def get_samples():
    sid = flask.session.get("id")
    s = db_SAMPLE.get(sid)
    tds = db_TDS.get(sid)
    if s is None or tds is None:
        raise TanswerSIDException
    return {"vectors": s, "elements": [tds.vec2element(v) for v in s]}


@app.route("/get/sample/<int:i>/")
def get_sample(i: int):
    sid = flask.session.get("id")
    s = db_SAMPLE.get(sid)
    tds = db_TDS.get(sid)

    if s is None or tds is None:
        raise TanswerSIDException

    if i >= len(s):
        return {"element": False}
    else:
        return {"vector": s[i], "element": tds.vec2element(s[i])}


@app.route("/get/element/<int:x>/<int:y>/")
def get_element(x: int, y: int):
    sid = flask.session.get("id")
    tds = db_TDS.get(sid)
    if tds is None:
        raise TanswerSIDException

    return tds.vec2element((x, y))


@app.route("/result/", methods=["POST"])
def result():
    sid = flask.session.get("id")
    tds = db_TDS.get(sid)
    if tds is None:
        raise TanswerSIDException

    return flask.render_template("result.html", result=json.loads(flask.request.form["result"]), tds=tds)


@app.route("/process-weight/", methods=["POST"])  # temporary
def process_weight():
    sid = flask.session.get("id")
    w = db_W.get(sid)
    w_name = db_W_name.get(sid)
    if w is None or w_name is None:
        raise TanswerSIDException

    ws = list(map(eval, flask.request.form.getlist("weight_add")))
    for e in ws:
        w[tuple(e)] += 1

    weight_is_save = flask.request.form.get("weight-is-save", False)
    if weight_is_save:
        name = flask.request.form.get("name", "")
        if name:
            save_weight(w, name)
    else:
        save_weight(w, w_name)
    return flask.redirect(flask.url_for("ready"))


def save_weight(x, name: str):
    name = os.path.splitext(name)[0]
    with open(os.path.join(os.getcwd(), "preference", "weight", "%s.pkl" % name), "wb") as f:
        pickle.dump(x, f)
    return True


@app.route("/save_as/")
def save_as():
    pass


if __name__ == '__main__':
    app.run(host=CONFIG["host"], port=CONFIG["port"], debug=CONFIG["debug"])
