import cv2
import numpy as np

img1 = cv2.imread('./chicken.jpg')
img2 = cv2.imread('./chicken2.jpg')

print(img1.shape)
print(img2.shape)
w,h,c=img2.shape
img1 = cv2.resize(img1,dsize=(h,w))
print(img1.shape)

roi = img2[0;row,0:cols]

img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_fg = cv2.bitwise_and(img1,img1,mask=mask)
img2_bg = cv2.bitwise_and(rot,roi,mask=mask_inv)

dst = cv2.add(img1_fg,img2_bg)

img2[0:w,0:h]=dst

cv2.imsh0ow('res',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
