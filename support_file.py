import requests
from pprint import pprint
import cv2
import time
import os

total_cars = 0

def get_frame(scen):
    #regions = ['in']
    cap1 = cv2.VideoCapture('video.avi')
    cap2 = cv2.VideoCapture('video.avi')
    cap3 = cv2.VideoCapture('video.avi')
    cap4 = cv2.VideoCapture('video.avi')

    car_cascade = cv2.CascadeClassifier('car_detect.xml') 

    while True:
        ret, frames1 = cap1.read() #extract video frame
        ret, frames2 = cap2.read() #extract video frame
        ret, frames3 = cap3.read() #extract video frame
        ret, frames4 = cap4.read() #extract video frame                        
        time.sleep(.2)
	
        gray1 = cv2.cvtColor(frames1, cv2.COLOR_BGR2GRAY) 
        gray2 = cv2.cvtColor(frames2, cv2.COLOR_BGR2GRAY) 	
        gray3 = cv2.cvtColor(frames3, cv2.COLOR_BGR2GRAY) 
        gray4 = cv2.cvtColor(frames4, cv2.COLOR_BGR2GRAY) 

        cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1)
        cars2 = car_cascade.detectMultiScale(gray2, 1.1, 1)
        cars3 = car_cascade.detectMultiScale(gray3, 1.1, 1)
        cars4 = car_cascade.detectMultiScale(gray4, 1.1, 1)

        total_cars1 = [len(cars1)]
        total_cars2 = [len(cars2)]
        total_cars3 = [len(cars3)]
        total_cars4 = [len(cars4)]
        """
        car = {'A':total_cars1,'B':total_cars2,'C':total_cars3,'D':total_cars4}
        sortedCar = [key for (key, value) in sorted(car.items(), key=lambda key_value: key_value[1])]
        if(sortedCar[0]=='A')
        """
        
                              

        #print("Total no of Cars = ",total_cars)
	
        for (x,y,w,h) in cars1:
            print(x)
        
            cv2.rectangle(frames1,(x,y),(x+w,y+h),(0,0,255),2)
        
            #cv2.imshow('video2', frames)
            cv2.putText(frames1,"Cars:"+ str(total_cars1),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv2.circle(frames1,(50,20),20,[0,255,0],-1)
            cv2.imwrite(os.path.join("static/images/","1.jpg"),frames1)

        for (x,y,w,h) in cars2:
            print(x)
        
            cv2.rectangle(frames2,(x,y),(x+w,y+h),(0,0,255),2)
        
            #cv2.imshow('video2', frames)
            cv2.putText(frames2,"Cars:"+ str(total_cars2),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv2.circle(frames2,(50,20),20,[0,255,0],-1)
            cv2.imwrite(os.path.join("static/images/","2.jpg"),frames2)

        for (x,y,w,h) in cars3:
            print(x)
        
            cv2.rectangle(frames3,(x,y),(x+w,y+h),(0,0,255),2)
        
            #cv2.imshow('video2', frames)
            cv2.putText(frames3,"Cars:"+ str(total_cars3),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)
            cv2.circle(frames3,(50,20),20,[0,255,0],-1)
            cv2.imwrite(os.path.join("static/images/","3.jpg"),frames3)

        for (x,y,w,h) in cars4:
            print(x)
        
            cv2.rectangle(frames4,(x,y),(x+w,y+h),(0,0,255),2)
        
            #cv2.imshow('video2', frames)
            cv2.putText(frames4,"Cars:"+ str(total_cars4),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
            cv2.circle(frames4,(50,20),20,[0,255,0],-1)
            cv2.imwrite(os.path.join("static/images/","4.jpg"),frames4)                                         
 
        imgencode=cv2.imencode('.jpg',frames1)[1]
        stringData=imgencode.tostring()
       
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cam.release()
    del(cam)

