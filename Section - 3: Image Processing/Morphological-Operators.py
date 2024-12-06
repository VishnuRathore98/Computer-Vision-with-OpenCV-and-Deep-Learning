## Morphological Operators

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    blank_img =np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale= 5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img = load_img()

display_img(img)

## Erosion

# Erodes away boundaries of foreground objects. Works best when foreground is light color (preferrably white) and background is dark.

kernel = np.ones((5,5),np.uint8)
erosion1 = cv2.erode(img,kernel,iterations = 1)

display_img(erosion1)

img = load_img()
kernel = np.ones((5,5),np.uint8)
erosion5 = cv2.erode(img,kernel,iterations = 4)

display_img(erosion5)

# ## Opening
# Opening is erosion followed by dilation. Useful in removing background noise!

img = load_img()

white_noise = np.random.randint(low=0,high=2,size=(600,600))

white_noise

white_noise = white_noise*255

white_noise.shape

img.shape

noise_img = white_noise+img

display_img(noise_img)

opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)

display_img(opening)

# ### Closing
#  Useful in removing noise from foreground objects, such as black dots on top of the white text.

img = load_img()

black_noise = np.random.randint(low=0,high=2,size=(600,600))

black_noise

black_noise= black_noise * -255

black_noise_img = img + black_noise

black_noise_img

black_noise_img[black_noise_img==-255] = 0

display_img(black_noise_img)

closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)

display_img(closing)

# ## Morphological Gradient
# 
# Difference between dilation and erosion of an image.

img = load_img()

display_img(img)

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

display_img(gradient)