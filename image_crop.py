#%%
import cv2
import json

img = cv2.imread("255065.jpg")

with open('255065.json') as json_file:
    json_data = json.load(json_file)
    
xMin=json_data[0]['xMin']
yMin=json_data[0]['yMin']
xMax=json_data[0]['xMax']
yMax=json_data[0]['yMax']

# crop = img[xMin:xMax,0:yMax]
# cv2.imshow('crop',crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 
# %%
crop = img[0:yMax,xMin:xMax]
cv2.imwrite("crop.jpg",crop)
# %%
from IPython.display import Image
Image(filename='crop.jpg') 
# %%
