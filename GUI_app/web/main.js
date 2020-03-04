function showOutput() {
    var data = document.getElementById("data").value
    eel.getMedUpdate(data)(setOutput)
}
function setOutput(result) {
    document.getElementById("output").innerHTML=result
}