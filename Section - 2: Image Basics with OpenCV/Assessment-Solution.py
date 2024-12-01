import numpy as np
import matplotlib.pyplot as plt
import cv2

# image = cv2.imread('../../Computer Vision Resources/Computer-Vision-with-Python/DATA/dog_backpack.jpg')
image = np.zeros((512,512,3))
drawing = False
ix, iy = -1,-1

def draw_circles(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(image, (ix,iy), (x,y), (0,255,0), 4)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(image, (ix,iy), (x,y), (0,255,0), 4)

cv2.namedWindow('bag_pack', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('bag_pack', draw_circles)

while True:
    cv2.imshow('bag_pack',image)

    if (cv2.waitKey(1) & 0xFF == 27):
        break

cv2.destroyAllWindows()