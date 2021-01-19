#%%
import cv2
import numpy as np
# %%
path = "./chicken.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(256,256))
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
# 
kernel = np.ones((3,3))
kernel = -kernel
kernel[1][1]=9
# Image Blurr

# [[-1. -1. -1.]
#  [-1.  9. -1.]
#  [-1. -1. -1.]]

print(kernel)

# %%

fileterd = cv2.filter2D(img,-1,kernel)
cv2.imshow("filtered",fileterd)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%