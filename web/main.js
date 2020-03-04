function showOutput() {
    var data = document.getElementById("data").nodeValue
    eel.getMedUpdate(data)(function(ret){console.log(ret)})
}