#this is comment

'''
gtryh
ghghgh
'''
"""
fgrfhtjt
rtrhgrgf
"""
import cv2 


cap = cv2.VideoCapture('video.avi')

car_cascade = cv2.CascadeClassifier('car_detect.xml') 

while True:
    
    ret, frames = cap.read() #extract video frame
	
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
	

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    total_cars = len(cars)

    print("Total no of Cars = ",total_cars)
	
    for (x,y,w,h) in cars:
        
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        
        cv2.imshow('video2', frames)
        
        if(x<100):
            print("wrong side vehicle dtected")
    if cv2.waitKey(33) == 27:
        break
                 
                 

cv2.destroyAllWindows() 
