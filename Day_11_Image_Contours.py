#%%
import cv2
import numpy as np

img = cv2.imread('contour.jpg')
img = cv2.resize(img,dsize=(500,500))
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 120,255,0)
# Contour는 list 형태로 반환
# hierachy 는 같은 level의 contour를 뜻함

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.CHAIN_APPROX_NONE 는 모든 point 저장
# cv2.CHAIN_APPROX_SIMPLE 4개의 point만 저장

image = cv2.drawContours(img, contours, -1, (0,255,0), 5)

print(contours)
print(hierachy)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
