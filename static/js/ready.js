let tds = JSON.parse(localStorage.getItem("temp-tds"));

let stage_selects = document.getElementById("stage_selects");

for (let i = 0; i < tds["stageMap"].length; i++) {
    let li = document.createElement("li")
    li.innerHTML = `${tds["stageMap"][i]}<input type=\"checkbox\" value=\"${i}\" name=\"selected-stages\">`
    stage_selects.appendChild(li);
}