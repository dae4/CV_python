#%%

import cv2
import numpy as np

path ="./chicken.jpg"
# %%
def salt_n_pepper(img,p):
    output = np.zeros(img.shape,np.uint8)
    thres = 1-p
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rand_n = np.random.randn()
            if rand_n < p:
                output[i][j]=0
            elif rand_n > thres:
                output[i][j]=255
            else:
                output[i][j]=img[i][j]
    return output

## Make Noise
img = cv2.imread(path)
img = cv2.resize(img,dsize=(300,300))
origin = np.copy(img)
noise_img = salt_n_pepper(img,0.2)
cv2.imshow("noise_img",noise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
# Apply Blur & Median Filter
blur = cv2.blur(noise_img,(3,3))
median = cv2.medianBlur(noise_img,5)
cv2.imshow("median",median)
cv2.imshow("blur",blur)
cv2.imshow("origin",origin)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
