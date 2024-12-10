import cv2

point = (0, 0)
buttonClicked = False


def button_click_handler(event, x, y, flags, param):
    global point, buttonClicked

    # When button click is registered
    if event == cv2.EVENT_LBUTTONDOWN:
        # Reset
        if buttonClicked == True:
            point = (0, 0)
            buttonClicked = False
        # Set
        if buttonClicked == False:
            point = (x, y)
            buttonClicked = True


cap = cv2.VideoCapture(0)

cv2.namedWindow('Make Circle')

cv2.setMouseCallback('Make Circle', button_click_handler)

while True:
    ret, frame = cap.read()

    if buttonClicked:
        cv2.circle(frame, point, 18, (0, 0, 255), 2)

    cv2.imshow('Make Circle', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
