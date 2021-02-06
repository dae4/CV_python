#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
## Use numpy

img = cv2.imread('chicken2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

hist, bins = np.histogram(img.flatten(),256,[0,255])

cdf = hist.cumsum()

cdf_m = np.ma.masked_equal(cdf,0)

cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(img2),plt.title('Equalization')
plt.show()
# %%
## Use CV
## only Grey channel
img = cv2.imread('chicken2.jpg',0);

# OpenCV의 Equaliztion함수
img2 = cv2.equalizeHist(img)
img = cv2.resize(img,(400,400))
img2 = cv2.resize(img2,(400,400))

dst = np.hstack((img, img2))
cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()
# %%
## CLAHE

img = cv2.imread('chicken2.jpg',0);

# contrast limit가 2이고 title의 size는 8X8
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img2 = clahe.apply(img)

img = cv2.resize(img,(400,400))
img2 = cv2.resize(img2,(400,400))

dst = np.hstack((img, img2))
cv2.imshow('img',dst)
cv2.waitKey()
cv2.destroyAllWindows()
