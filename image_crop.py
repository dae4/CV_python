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

crop = img[0:yMax,xMin:xMax]
cv2.imwrite("crop.jpg",crop)
# %%
from PIL import Image,ImageDraw
import numpy as np

origin_img=Image.open('crop.jpg')

width,height = origin_img.size

lum_img = Image.new('L', [width,height] , 0)
draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0,0), (width,height)], 0, 360, fill = 1, outline = "white")
img_arr =np.array(origin_img)
## background
lum_img_arr =np.array(lum_img)[...,np.newaxis]
lum_back_arr = (1- lum_img_arr)*255
lum_back_arr = np.dstack([lum_back_arr,lum_back_arr,lum_back_arr])
## imgae 
final_img_arr = img_arr*lum_img_arr
final_img_arr = final_img_arr+ lum_back_arr

final_img = Image.fromarray(final_img_arr)
final_img.save('circle.jpg')
# %%
