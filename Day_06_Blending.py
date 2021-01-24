#%%

import cv2
import numpy as np

img1 = cv2.imread('./chicken.jpg')
img2 = cv2.imread('./chicken2.jpg')

print(img1.shape)
print(img2.shape)
#%%
## resize img1
w,h,c=img2.shape

img1 = cv2.resize(img1,dsize=(h,w))

print(img1.shape)
#%%
def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('w','image',0,100,nothing)
#%%
while True:
    w = cv2.getTrackbarPos('w','image')
    dst = cv2.addWeighted(img1,float(100-w)*0.01,img2,float(w)*0.01,0)
    cv2.imshow('dst',dst)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
# %%
