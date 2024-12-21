import cv2

face_cascade = cv2.CascadeClassifier(
    '../DATA/haarcascades/haarcascade_frontalface_default.xml')


def detect_face(frame):
    face_rects = face_cascade.detectMultiScale(frame)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 10)
    return frame


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)  # type: ignore
    frame = detect_face(frame)
    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
