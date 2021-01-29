#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

#cv.sobel(src,ddepth,dx,dy,ksize)

img = cv2.imread('chicken.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

canny = cv2.Canny(img,30,70)

laplacian = cv2.Laplacian(img,cv2.CV_8U)

SobelX = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)

SobelY = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

images = [img,laplacian,SobelX,SobelY,canny]
titles = ["img","laplacian","SobelX","SobelY","canny"]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()
# %%
