## Image Pyramids 
## Image pyramids란 동일 이미지의 서로 다른 사이즈의 set을 Image Pyramids라고 함. 
## 보통 가장 아래에 큰 해상도를 놓고 점점 크기를 줄여가면서 쌓아가는 형태임
## 1) Gaussian Pyramids, 2) Laplacian Pyramids
#%%
import cv2

img = cv2.imread("chicken.jpg")
img = cv2.resize(img,dsize=(225,225))
lower_reso = cv2.pyrDown(img)
higher_reso = cv2.pyrUp(img)

print(img.shape)
print(lower_reso.shape)
print(higher_reso.shape)

cv2.imshow('img',img)
cv2.imshow('lower',lower_reso)
cv2.imshow("higher",higher_reso)

cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
# restore image

# image scale down
higher_reso = cv2.pyrDown(higher_reso)
# image scale up
lower_reso = cv2.pyrUp(lower_reso)

print(img.shape)
print(lower_reso.shape)
print(higher_reso.shape)
# (225, 225, 3)
# (226, 226, 3)
# (225, 225, 3)
