from tkinter import Frame
import cv2

cascade_wajah = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

while True:
    _, Frame = cam.read()
    gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    faces = cascade_wajah.detectMultiScale(gray, 1.3,3)
    for x, y, w, h in faces:
        cv2.rectangle(Frame, (x,y),(x+w, y+h), (0,255,0))

    cv2.imshow("Deteksi Wajah", Frame)

    if cv2. waitKey(1) & 0xff == ord("x"):
        break

cam.release()
cv2.destroyAllWindows()


