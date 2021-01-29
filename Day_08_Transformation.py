#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("chicken.jpg")
#opencv read BGR color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

w,h,c = img.shape

pts1 = np.float32([[200,100],[400,100],[200,200]])
pts2 = np.float32([[200,300],[400,200],[200,400]])

#draw circle
cv2.circle(img, (200,100),10,(255,0,0),-1)
cv2.circle(img, (400,100),10,(0,255,0),-1)
cv2.circle(img, (200,200),10,(0,0,255),-1)
# Affine Transformation

# Affine Tranformation Matrix
# M = cv2.getAffineTransform(변환 전 픽셀 좌표, 변환 후 픽셀 좌표)
M = cv2.getAffineTransform(pts1,pts2)
# 결과 배열 = cv2.warpAffine(원본 배열 행렬, 결과 배열의 크기, 보간법, 테두리 외삽법, 테두리 색상)
dst = cv2.warpAffine(img,M,(h,w))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Affine')
plt.show()
# %%

#Perspective Transformation

pts1 = np.float32([[222,469],[200,1920],[1070,454],[1154,1944]])
pts2 = np.float32([[250,450],[200,1900],[1050,450],[1050,1900]])

cv2.circle(img, (222,469),50,(255,0,0),-1)
cv2.circle(img, (200,1920),50,(0,255,0),-1)
cv2.circle(img, (1154,1944),50,(0,0,255),-1)
cv2.circle(img, (1070,454),50,(0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (h,w))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
plt.show()
# %%
