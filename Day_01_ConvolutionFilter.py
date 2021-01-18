#%%
import cv2
import numpy as np
## Read image
im_path='./chicken.jpg'
img=cv2.imread(im_path,2)

# Resize & show

img = cv2.resize(img,(299,299))
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%

# Apply filter

kernel =np.random.rand(3,3)
print(kernel)

kernel2=np.array([[0,1,0],[1,1,1],[0,1,0]])
print(kernel2) 

filtered_img = cv2.filter2D(img,-1,kernel2)

# void filter2D(InputArray src, OutputArray dst, int ddepth, InputArray kernel, Point anchor=Point(-1,-1), double delta=0, int borderType=BORDER_DEFAULT )

# • src – 입력 영상

# • dst – 입력 영상과 크기, 채널수가 동일한 결과 영상.

# • ddepth – 원하는 결과 영상의 깊이(depth), 만약 음수일 경우 src.depth()와 동일, src.depth()와 ddepth는 아래와 같은 조합이 가능하다:

# • src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F

# • src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F

# • src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F

# • src.depth() = CV_64F, ddepth = -1/CV_64F

# • kernel – convolution할 커널, 또는 correlation 커널로써 부동 소수점 단일 채널 행렬(Matrix)이다. 만약 채널별로 다른 커널을 적용하고 싶다면, split() 함수를 이용하여 채널별로 나눈 후 독립적으로 커널을 적용해야 한다.

# • anchor – anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; default value (-1,-1) means that the anchor is at the kernel center.

# • delta – 옵션으로, 필터 적용 후에 픽셀에 더해질 value 을 의미

# • borderType – 이미지의 테두리 부분을 처리할 메소드

cv2.imshow("img",img)
cv2.imshow("filtered_img",filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


 # %%
