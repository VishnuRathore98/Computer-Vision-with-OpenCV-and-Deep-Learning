import cv2
import numpy as np
import matplotlib.pyplot as plt

gorilla = cv2.imread('../DATA/gorilla.jpg', 0)


def display(img, cmap=None):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)


hist_values = cv2.calcHist([gorilla], channels=[0],
                           mask=None, histSize=[256], ranges=[0, 256])

eq_gorilla = cv2.equalizeHist(gorilla)

hist_values = cv2.calcHist([eq_gorilla], channels=[
                           0], mask=None, histSize=[256], ranges=[0, 256])

plt.plot(hist_values)

color_gorilla = cv2.imread('../DATA/gorilla.jpg')
show_gorilla = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2RGB)

# Convert to HSV colorspace
hsv = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2HSV)

# Grab V channel and equalize
hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])

# Convert back to RGB to visualize
eq_color_gorilla = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
