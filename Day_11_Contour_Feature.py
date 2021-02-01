#%%
import cv2
import numpy as np

img = cv2.imread('contour.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,100,255,0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 첫번째 contours의 moment 특징 추출
cnt = contours[0]
# cv2.moments 는 모멘트를 구하는 함수로 모멘트함수를 통해 면적, 평균, 분산 을 쉽게 구할 수 있음 
M = cv2.moments(cnt)

print(M.items())
## cx, cy는 중심점.  
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
# %%
## 면적
print(cv2.contourArea(cnt))
# %%
# cv2.arcLength(cnt, True)
# True일때 폐곡선을 그리고 둘레, False일때 시작점부터 끝점까지 둘레
print(cv2.arcLength(cnt, True))
print(cv2.arcLength(cnt, False))
# %%
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hands.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = img.copy()
img2 = img.copy()
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,150,200,cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cntnum=0
# 가장 긴 contour 찾기
for contuor in contours:
    if cntnum < len(contuor):
        cntnum = len(contuor)
        cnt = contuor

# 적용하는 숫자가 커질 수록 Point의 갯수는 감소
epsilon1 = 0.01*cv2.arcLength(cnt, True)
epsilon2 = 0.1*cv2.arcLength(cnt, True)

approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

print(len(cnt))
print(len(approx1))
print(len(approx2))

cv2.drawContours(img, [cnt],0,(0,255,0),3) # 487개의 Point
cv2.drawContours(img1, [approx1], 0,(0,255,0), 3) # 17개의 Point
cv2.drawContours(img2, [approx2], 0,(0,255,0), 3) # 2개의 Point

titles = ['Original', '1%', '10%']
images = [img, img1, img2]

for i in range(3):
    plt.subplot(1,3,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# %%
