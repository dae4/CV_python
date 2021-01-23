#%%
import cv2
import numpy as np

img = cv2.imread("chicken.jpg")

# shape of img
print(img.shape)

# number of img pixel
print(img.size)

# type of img
print(img.dtype)

## image ROI
chicken = img[400:1800,300:1100]
cv2.imshow("chicken",chicken)
cv2.waitKey(0)
cv2.destroyAllWindows() 
# %%
# Red channel 0
chicken[:,:,2] = 0
cv2.imshow("chicken_red",chicken)
cv2.waitKey(0)
cv2.destroyAllWindows() 
# %%
