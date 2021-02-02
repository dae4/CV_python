#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hands.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = img.copy()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,150,200,cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cntnum=0
# 가장 긴 contour 찾기
for contuor in contours:
    if cntnum < len(contuor):
        cntnum = len(contuor)
        cnt = contuor

hull = cv2.convexHull(cnt)

cv2.drawContours(img1, [hull], 0,(0,255,0), 3)

titles = ['Original','Convex Hull']
images = [img, img1]

for i in range(2):
    plt.subplot(1,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])
plt.savefig("Convex_Hull.jpg")
plt.show()
# %%
