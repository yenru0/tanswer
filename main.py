import json
import glob
import pickle
import os

import flask

import function.structure.data
from function.reader.exceptions import ReaderWrongException
from function.structure.exceptions import TDSEmptyException

app = flask.Flask("tanswer")

### config
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
app.jinja_env.globals.update(
    zip=zip, enumerate=enumerate, len=len
)

app.secret_key = b"the best i know is juhajin"

# temporary use this variable to save
U: function.structure.data.TanswerDataStruct = None
S: list = None
X = None
X_name: str = "W.pkl"


@app.route("/")
def front():
    return flask.render_template("front.html")


@app.route("/select/", methods=["GET"])
def select():
    global U
    files = [os.path.basename(f) for f in glob.glob(os.path.join(os.getcwd(), 'dataset', "*.tnw"))]
    return flask.render_template("select.html", files=files)


@app.route("/fast_start/", methods=["GET"])
def fast_start():
    return flask.render_template("fast_start.html")


@app.route("/compile/", methods=["POST"])
def compile():
    global U
    # code for something compile
    if "file" in flask.request.files:
        f = flask.request.files["file"]
        if f.filename == '':
            return flask.redirect(flask.url_for("ready"))
        try:
            U = function.structure.data.TanswerDataStruct(f.read().decode("utf-8"), "", "")
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
                U = function.structure.data.TanswerDataStruct(f.read(), "", "")
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
    global U
    warn_message = flask.request.args.get("warn_message", None)
    weights = [os.path.basename(f) for f in glob.glob(os.path.join(os.getcwd(), "preference", "weight", "*.pkl"))]
    return flask.render_template("ready.html", tds=U, weights=weights, warn_message=warn_message)


@app.route("/start/", methods=["POST"])
def start():
    global U
    global S
    global X
    global X_name

    # get weight
    weight_is_default = flask.request.form.get("weight-is-default")
    X_name = ""
    if weight_is_default:
        try:
            weight_default_value = int(flask.request.form.get("weight-default-value"))
            if 1 <= weight_default_value <= 100:
                X = U.make_init_weight(default=weight_default_value)
        except Exception:
            X = U.make_init_weight()
    else:
        selected_weight = flask.request.form.get("selected-weight")
        if selected_weight:
            with open(os.path.join(os.getcwd(), "preference", "weight", selected_weight), 'rb') as f:
                try:
                    X = pickle.load(f)
                except (EOFError, pickle.PickleError):
                    X = None
            X_name = selected_weight
        else:
            X = U.make_init_weight()
    if not X_name:
        X_name = "W.pkl"

    # weight validity check
    if not U.valid(X):
        return flask.redirect(flask.url_for("ready", warn_message="Invalid Weight Object"))

    wil = int(flask.request.form.get("wil"))
    if wil < 0:
        return flask.redirect(flask.url_for("ready", warn_message="Invalid Wil(number of repeat)"))
    stgs = list(map(int, flask.request.form.getlist("selected-stages")))
    S = U.sampling(wil, X, stages=stgs)
    return flask.render_template("start.html", samples=S)


@app.route("/get/samples/")
def get_samples():
    return {"vectors": S, "elements": [U.vec2element(v) for v in S]}


@app.route("/get/sample/<int:i>/")
def get_sample(i: int):
    global S
    if i >= len(S):
        return {"element": False}
    else:
        return {"vector": S[i], "element": U.vec2element(S[i])}


@app.route("/get/element/<int:x>/<int:y>/")
def get_element(x: int, y: int):
    global U
    return U.vec2element((x, y))


@app.route("/result/", methods=["POST"])
def result():
    global U
    return flask.render_template("result.html", result=json.loads(flask.request.form["result"]), tds=U)


@app.route("/process-weight/", methods=["POST"])  # temporary
def process_weight():
    global X
    ws = list(map(eval, flask.request.form.getlist("weight_add")))
    for w in ws:
        X[tuple(w)] += 1
    weight_is_save = flask.request.form.get("weight-is-save", False)
    if weight_is_save:
        name = flask.request.form.get("name", "")
        if name:
            save_weight(X, name)
    else:
        save_weight(X, X_name)
    return flask.redirect(flask.url_for("ready"))


def save_weight(x, name: str):
    name = os.path.splitext(name)[0]
    with open(os.path.join(os.getcwd(), "preference", "weight", "%s.pkl" % name), "wb") as f:
        pickle.dump(x, f)
    return True


@app.route("/save_as/")
def save_as():
    global X


if __name__ == '__main__':
    debug = False
    if not os.path.isdir("./dataset"):
        os.mkdir("./dataset")
    if not os.path.isdir("./preference"):
        os.mkdir("./preference")

    app.run(debug=debug)
