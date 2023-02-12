import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

while True:

    _, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 10)

    for (x, y, h, w) in faces:

        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('FaceDetection', img)
    k = cv2.waitKey(30)
    
    if k == 27:
        break

