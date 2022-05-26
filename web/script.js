
var status = 1
function py_video(self) {
    var data = self.getAttribute('elem-data')
    if (data == "start"){
        status = 1
        self.setAttribute("elem-data", "stop")
        self.style.background = "#dc3545"
        self.textContent = "Stop"
        document.querySelector(".loader").style.display = "block"
        var optionsSelected = selectedOption()
        eel.startVideo(optionsSelected)()
    }
    else {
        status = 0
        self.setAttribute("elem-data", "start")
        self.style.background = "#28a745"
        self.textContent = "Start"
    }
   
}

function selectedOption(){
    var faceDetection = document.querySelector("#faceDetection").checked
    var eyeDetection = document.querySelector("#eyeDetection").checked
    return {"face":faceDetection, "eye":eyeDetection}
}





eel.expose(updateImageSrc);
function updateImageSrc(imageBase64) {
    document.querySelector(".loader").style.display = "none"
    let elem = document.getElementById('bg');
    elem.src = "data:image/jpg;base64," + imageBase64
    return status
}


eel.expose(stopValue)
function stopValue(){
    return status
}