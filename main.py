import json
import os

import flask

import function.structure.data
from function.reader.exceptions import ReaderWrongException
from function.structure.exceptions import TDSEmptyException
import pickle

app = flask.Flask("tanswer")

### config
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
app.jinja_env.globals.update(
    zip=zip, enumerate=enumerate, len=len
)

app.secret_key = b"the best i know is juhajin"

# temporary use this variable to save
U: function.structure.data.TanswerDataStruct = None


@app.route("/")
def front():
    return flask.render_template("front.html")


@app.route("/fast_start/", methods=["GET", "POST"])
def fast_start():
    global U
    global X
    if flask.request.method == 'POST':
        if "file" not in flask.request.files:
            return "wrong"
        f = flask.request.files["file"]

        # when file doesn't exist
        if f.filename == '':
            return flask.render_template("fast_start.html")

        # check if file is normally accepted
        try:
            U = function.structure.data.TanswerDataStruct(f.read().decode('utf-8'), "temp", "temp is tempting")
            if X is None:
                X = U.make_init_weight()
        except ReaderWrongException:
            return "reader wrong"
        except UnicodeDecodeError:
            return "not unicode text"
        except TDSEmptyException:
            return "tds empty exception"

        return flask.redirect(flask.url_for("ready"), code=307, )
    else:
        return flask.render_template("fast_start.html")


@app.route("/ready/", methods=["GET", "POST"])
def ready():
    global U
    if flask.request.method == 'GET':
        # do not reach at now
        return flask.render_template("ready.html", tds=U.dict)
    else:  # post
        return flask.render_template("ready.html", tds=U.dict)


@app.route("/start/", methods=["POST"])
def start():
    wil = int(flask.request.form.get("wil"))
    if wil < 0:
        return flask.redirect(flask.url_for("ready"))
    stgs = list(map(int, flask.request.form.getlist("selected-stages")))
    samples = U.sampling(wil, weight=X, stages=stgs)
    flask.session["temp-tds-samples"] = samples
    return flask.render_template("start.html", samples=samples)


@app.route("/get/samples/")
def get_samples():
    samples = flask.session["temp-tds-samples"]
    return {"vectors": samples, "elements": [U.vec2element(v) for v in samples]}


@app.route("/get/sample/<int:i>/")
def get_sample(i: int):
    sample = flask.session["temp-tds-samples"]
    if i >= len(sample):
        return {"element": False}
    else:
        return {"vector": sample[i], "element": U.vec2element(sample[i])}


@app.route("/get/element/<int:x>/<int:y>/")
def get_element(x: int, y: int):
    return U.vec2element((x, y))


@app.route("/select/")
def select():
    pass


@app.route("/result/", methods=["post"])
def result():
    return flask.render_template("result.html", result=json.loads(flask.request.form["result"]), tds=U)


@app.route("/add_w/", methods=["post"])  # temporary
def add_w():
    # will be corrected
    ws = list(map(eval, flask.request.form.getlist("weight_add")))
    for w in ws:
        X[tuple(w)] += 1
    return flask.redirect(flask.url_for("ready"))


@app.route("/save/")
def save():
    with open(os.getcwd() + "/preference/W.pkl", "wb") as f:
        pickle.dump(X, f)
    return "saved"


if __name__ == '__main__':
    import os

    X = None
    if os.path.isfile("./preference/W.pkl"):
        with open("./preference/W.pkl", "rb") as f:
            X = pickle.load(f)

    if not os.path.isdir("./dataset"):
        os.mkdir("./dataset")
    if not os.path.isdir("./preference"):
        os.mkdir("./preference")

    app.run(debug=False)
