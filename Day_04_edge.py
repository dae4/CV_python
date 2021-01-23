#%%
import cv2

img_path="./chicken.jpg"

img = cv2.imread(img_path)
img = cv2.resize(img,(500,500))
sobel = cv2.Sobel(img,-1,1,1,ksize=3)
laplacian = cv2.Laplacian(img,-1,ksize=3)
cv2.imshow("sobel",sobel)
cv2.imshow("laplacian",laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
