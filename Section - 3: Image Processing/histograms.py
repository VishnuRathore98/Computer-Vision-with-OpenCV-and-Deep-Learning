# Image Histograms with OpenCV

import cv2
import matplotlib.pyplot as plt

blue_bricks = cv2.imread('../DATA/bricks.jpg')
show_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)

# OpenCV Histogram
hist_values = cv2.calcHist([blue_bricks], channels=[
                           0], mask=None, histSize=[256], ranges=[0, 256])

# plt.plot(hist_values)
# plt.show()

# Plotting 3 Color Histograms
img = blue_bricks
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title('Blue Bricks Image')
plt.show()
