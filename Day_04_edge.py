#%%
import cv2

img_path="./chicken"

img = cv2.imread(img_path)
res = cv2.Sobel(img,-1,1,1,ksize=3)
cv2.imshow("edge",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
