import cv2 as cv

path = "D:\\ML\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml"
face_cascade = cv.CascadeClassifier(path)

video = cv.VideoCapture(0, cv.CAP_DSHOW)
#video = cv.VideoCapture("E:\lips\Data set\lucky.mp4")

a = 1
while True:
    a = a+1
    check, frame = video.read()
    print(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=5)
    for x, y, w, h in faces:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 55, 0), 3)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break



