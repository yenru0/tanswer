import json

import flask

import function.structure.data
from function.reader.exceptions import ReaderWrongException

app = flask.Flask("tanswer")

### config
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024
app.jinja_env.globals.update(
    zip=zip, enumerate=enumerate, len=len
)

app.secret_key = b"the best i know is juhajin"


@app.route("/")
def front():
    return flask.render_template("front.html")


@app.route("/fast_start/", methods=["GET", "POST"])
def fast_start():
    if flask.request.method == 'POST':
        if "file" not in flask.request.files:
            return "wrong"
        f = flask.request.files["file"]
        try:
            T = function.structure.data.TanswerDataStruct(f.read().decode('utf-8'), "temp", "temp is tempting")
        except ReaderWrongException:
            return "reader wrong"
        flask.session["temp-tds"] = T.dict

        # 분기 file이 가능하면 혹은 안가능하면
        return flask.redirect(flask.url_for("ready"), code=307, )
    else:
        return flask.render_template("fast_start.html")


@app.route("/ready/", methods=["GET", "POST"])
def ready():
    if flask.request.method == 'GET':
        if "temp-tds" in flask.session:
            T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
            return flask.render_template("ready.html", tds=T)
    else:
        if "temp-tds" in flask.session:
            T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
            return flask.render_template("ready.html", tds=T)
        else:
            return "wrong"


@app.route("/start/", methods=["POST"])
def start():
    wil = int(flask.request.form.get("wil"))
    if wil < 0:
        return flask.redirect(flask.url_for("ready"))
    stgs = list(map(int, flask.request.form.getlist("selected-stages")))
    T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
    samples = T.sampling(wil, weight=T.make_init_weight(), stages=stgs)
    flask.session["temp-tds-samples"] = samples
    return flask.render_template("start.html", samples=samples, tds=T)


@app.route("/get/samples/")
def get_samples():
    T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
    samples = flask.session["temp-tds-samples"]
    return {"vectors": samples, "elements": [T.vec2element(v) for v in samples]}


@app.route("/get/sample/<int:i>/")
def get_sample(i: int):
    T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
    sample = flask.session["temp-tds-samples"]
    if i >= len(sample):
        return {"element": False}
    else:
        return {"vector": sample[i], "element": T.vec2element(sample[i])}


@app.route("/get/element/<int:x>/<int:y>/")
def get_element(x: int, y: int):
    T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
    return T.vec2element((x, y))


@app.route("/select/")
def select():
    pass


@app.route("/result/", methods=["post"])
def result():
    T = function.structure.data.TanswerDataStruct("", "", "", ser=flask.session["temp-tds"])
    return flask.render_template("result.html", result=json.loads(flask.request.form["result"]), tds=T)


if __name__ == '__main__':
    import os

    if not os.path.isdir("./dataset"):
        os.mkdir("./dataset")
    if not os.path.isdir("./preference"):
        os.mkdir("./preference")

    app.run(debug=True)
