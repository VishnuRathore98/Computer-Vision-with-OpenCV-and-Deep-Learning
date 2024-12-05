
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    img = cv2.imread('../DATA/bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)


i = load_img()
display_img(i)


# -------

# ### Gamma Correction : Practical Effect of Increasing Brightness

img = load_img()
gamma = 1/4
effected_image = np.power(img, gamma)
display_img(effected_image)


img = load_img()
gamma = 2
effected_image = np.power(img, gamma)
display_img(effected_image)


# ### Low Pass Filter with a 2D Convolution
# 
# A fitlering operation known as 2D convolution can be used to create a low-pass filter. Make sure to view the video for an explanation of what's happening in the code below.


img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600), fontFace=font,fontScale= 10,color=(255,0,0),thickness=4)
display_img(img)


# ### Create the Kernel

kernel = np.ones(shape=(5,5),dtype=np.float32)/25

 
kernel

 
dst = cv2.filter2D(img,-1,kernel)
display_img(dst)

   
# ## Averaging

 
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600), fontFace=font,fontScale= 10,color=(255,0,0),thickness=4)
display_img(img)

 
blurred_img = cv2.blur(img,ksize=(5,5))

 
display_img(blurred_img)

   
# ## Gaussian Blurring

 
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600), fontFace=font,fontScale= 10,color=(255,0,0),thickness=4)
display_img(img)

 
blurred_img = cv2.GaussianBlur(img,(5,5),10)
display_img(blurred_img)

   
# ## Median Blurring

 
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600), fontFace=font,fontScale= 10,color=(255,0,0),thickness=4)
display_img(img)

 
median = cv2.medianBlur(img,5)
display_img(median)

   
# ----------
# ### Adding Noise
# 
# Let's see a more useful case of Median Blurring by adding some random noise to an image.

 
img = cv2.imread('../DATA/sammy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

 
img.max()

 
img.min()


img.mean()


img.shape


display_img(img)


noise_img = cv2.imread('../DATA/sammy_noise.jpg')


display_img(noise_img)


median = cv2.medianBlur(noise_img,5)
display_img(median)


# --------


# ## Bilateral Filtering


img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600), fontFace=font,fontScale= 10,color=(255,0,0),thickness=4)
display_img(img)

blur = cv2.bilateralFilter(img,9,75,75)


display_img(blur)


