let now = 0;
let nowVector;

let samples = [];
let elements = [];
let result = [];

let wil = -1;

function refresh() {
    document.getElementById("tanswer_progress").setAttribute("value", now);
    if (now >= wil) {
        document.getElementById("submit_next").disabled = true;

        let form = document.getElementById("form_result")
        let input = document.createElement("input");

        input.setAttribute("type", "hidden");
        input.setAttribute("name", "result");
        input.setAttribute("value", JSON.stringify(result));

        let el = document.createElement("input");
        el.setAttribute("type", "submit");

        form.appendChild(input);
        form.appendChild(el);
    } else {
        document.getElementById("question").innerText = elements[now][0][0][0];
        document.getElementById("answer").value = "";
        //document.getElementById("answer").innerText = json["element"][1].toString();
    }
    document.getElementById("tanswer_progress").setAttribute("value", now);
    nowVector = samples[now];

}

function next_fresh() {
    now += 1;
    result.push({"vector": nowVector, "answer": document.getElementById("answer").value});
    refresh();
}

//refresh();

// init

fetch("/get/samples/").then(function (response) {
    return response.json();
}).then(
    function (json) {
        samples = json["vectors"];
        elements = json["elements"];
        wil = samples.length;
        refresh();
    }
)