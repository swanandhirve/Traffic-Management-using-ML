import cv2
import os

cap1 = cv2.VideoCapture('video.avi')
i=1
while True:
    ret, frames1 = cap1.read()
    cv2.imwrite(os.path.join("frames/images/",str(i)+".jpg"),frames1)
                
    i=i+1
