import cv2
import eel
import base64
import time
import sys
import threading



class capture():
    def __init__(self, optionsSelected):
        self.faceSelected = optionsSelected["face"]
        self.eyeSelected = optionsSelected["eye"]
        print(self.faceSelected, self.eyeSelected)

        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

    status = 1
    def draw_found(self, detected, image, color: tuple):
        for (x, y, width, height) in detected:
            cv2.rectangle(
                image,
                (x, y),
                (x + width, y + height),
                color,
                thickness=2
            )

    def genImg(self):
        if self.faceSelected == True and self.eyeSelected == True:
            while True:
                _, image = self.video.read()
                image = cv2.flip(image, 1)

                grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #detected_faces = self.face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)

                detected_faces = self.face_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
                detected_eyes = self.eye_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
                self.draw_found(detected_faces, image, (0, 0, 255))
                self.draw_found(detected_eyes, image, (0, 255, 0))


                _, jpeg = cv2.imencode('.jpg', image)
                jpgBytes = jpeg.tobytes()
                self.getImg(jpgBytes)

                stopStatus = eel.stopValue()()
                if stopStatus == '0':
                    break
        elif self.faceSelected == True and self.eyeSelected == False:
            while True:
                _, image = self.video.read()
                image = cv2.flip(image, 1)

                grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #detected_faces = self.face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)

                detected_faces = self.face_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
                self.draw_found(detected_faces, image, (0, 0, 255))

                _, jpeg = cv2.imencode('.jpg', image)
                jpgBytes = jpeg.tobytes()
                self.getImg(jpgBytes)

                stopStatus = eel.stopValue()()
                if stopStatus == '0':
                    break
        elif self.faceSelected == False and self.eyeSelected == True:
            while True:
                _, image = self.video.read()
                image = cv2.flip(image, 1)

                grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #detected_faces = self.face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=4)

                detected_eyes = self.eye_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
                self.draw_found(detected_eyes, image, (0, 255, 0))


                _, jpeg = cv2.imencode('.jpg', image)
                jpgBytes = jpeg.tobytes()
                self.getImg(jpgBytes)

                stopStatus = eel.stopValue()()
                if stopStatus == '0':
                    break

        else:
            while True:
                _, image = self.video.read()
                image = cv2.flip(image, 1)

                _, jpeg = cv2.imencode('.jpg', image)
                jpgBytes = jpeg.tobytes()
                self.getImg(jpgBytes)

                stopStatus = eel.stopValue()()
                if stopStatus == '0':
                    break

        self.video.release()

    def getImg(self, jpgBytes):
        imageBase64 = base64.b64encode(jpgBytes)
        imageDecoded = imageBase64.decode("utf-8")
        eel.updateImageSrc(imageDecoded)()


@eel.expose
def startVideo(optionsSelected):
    global videoRun
    videoRun = capture(optionsSelected)
    videoRun.genImg()

    


def start_app():
    # Start the server
    try:
        mainPage = 'main.html'
        eel.init("web")
        eel.start(mainPage)
        print("App Started")

    except Exception as e:
        print(f"couldn't start app!\nThe error: {e}")


if __name__ == "__main__":
    start_app()