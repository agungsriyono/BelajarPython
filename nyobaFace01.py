import cv2

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Kamera 1", img)
    cv2.imshow("Kamera 2", gray)
    if cv2. waitKey(1) & 0xff == ord("x"):
        break

cam.release()
cv2.destroyAllWindows()



