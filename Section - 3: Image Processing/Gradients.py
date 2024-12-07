import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../DATA/sudoku.jpg',0)

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

display_img(img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
laplacian = cv2.Laplacian(img,cv2.CV_64F)

display_img(sobelx)

display_img(sobely)

display_img(laplacian)

# Combining Previous Ideas

# Blending Images

blended = cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)

display_img(blended)

blended.shape

# Morphological Operators

kernel = np.ones((4,4),np.uint8)
gradient = cv2.morphologyEx(blended,cv2.MORPH_GRADIENT,kernel)

display_img(gradient)

# Try it on the laplacian result!

kernel = np.ones((3,3),np.uint8)
gradient = cv2.morphologyEx(blended,cv2.MORPH_GRADIENT,kernel)

display_img(gradient)

# Thresholds

ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
display_img(th1)

ret,th1 = cv2.threshold(gradient,200,255,cv2.THRESH_BINARY_INV)
display_img(th1)

ret,th1 = cv2.threshold(blended,100,255,cv2.THRESH_BINARY_INV)
display_img(th1)