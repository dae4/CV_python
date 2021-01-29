#%%
# object tracking using HSV color
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(True):
    ret, frame = cap.read()
    if ret :
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([30,50,50])
        upper_blue = np.array([200,255,255])

        mask = cv2.inRange(hsv,lower_blue,upper_blue)
        # inRange(color_space,lower_value,upper_value)
        res = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
# %%
