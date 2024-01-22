from flask import Flask, render_template, redirect, url_for, request,session,Response
from support_file import get_frame
import os
import cv2

car_cascade = cv2.CascadeClassifier('car_detect.xml') 
app = Flask(__name__)

app.secret_key = '1234'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('traffic'))
    return render_template('login.html', error=error)

@app.route('/option',methods=['GET', 'POST'])
def option():
    if request.method == 'POST':
        if request.form['scen'] == 'Wrong Side Vehicle':
            print('Wrong Side Vehicle')
            session['scen'] = request.form['scen']
            return redirect(url_for('vehicle'))

        elif request.form['scen'] == 'Unauthorized Vehicle':
            print('Unauthorized Vehicle')
            session['scen'] = request.form['scen']
            return redirect(url_for('vehicle'))

    return render_template('option.html')


@app.route('/vehicle')
def vehicle():
    #scen = session.get('scen',None)
    #print(scen)
    return render_template('vehicle.html')

@app.route('/traffic',methods=['GET', 'POST'])
def traffic():
    if request.method == 'POST':
        R = [0,0,255]
        G = [0,255,0]
        O = [22,180,231]

        if request.form['scenNo'] == '1':
            img1 = cv2.imread(os.path.join("static/images/1/","1.jpg"))
            img2 = cv2.imread(os.path.join("static/images/1/","2.jpg"))
            img3 = cv2.imread(os.path.join("static/images/1/","3.jpg"))
            img4 = cv2.imread(os.path.join("static/images/1/","4.jpg"))
        elif request.form['scenNo'] == '2': 
            img1 = cv2.imread(os.path.join("static/images/2/","1.jpg"))
            img2 = cv2.imread(os.path.join("static/images/2/","2.jpg"))
            img3 = cv2.imread(os.path.join("static/images/2/","3.jpg"))
            img4 = cv2.imread(os.path.join("static/images/2/","4.jpg"))

        #cv2.imwrite(os.path.join("static/images/","1.jpg"),img1)
        #cv2.imwrite(os.path.join("static/images/","2.jpg"),img2)
        #cv2.imwrite(os.path.join("static/images/","3.jpg"),img3)
        #cv2.imwrite(os.path.join("static/images/","4.jpg"),img4)

        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) 	
        gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY) 
        gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY) 

        cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1)
        cars2 = car_cascade.detectMultiScale(gray2, 1.1, 1)
        cars3 = car_cascade.detectMultiScale(gray3, 1.1, 1)
        cars4 = car_cascade.detectMultiScale(gray4, 1.1, 1)

        total_cars1 = len(cars1)
        total_cars2 = len(cars2)
        total_cars3 = len(cars3)
        total_cars4 = len(cars4)

        total = total_cars1+total_cars2+total_cars3+total_cars4

        T1 = (total_cars1/total) * 60
        T2 = (total_cars2/total) * 60
        T3 = (total_cars3/total) * 60
        T4 = (total_cars4/total) * 60                       

        car = {'A':total_cars1,'B':total_cars2,'C':total_cars3,'D':total_cars4}
        sortedcar = [key for (key, value) in sorted(car.items(), key=lambda key_value: key_value[1],reverse=True)]
        if(sortedcar[0]=='A'):
            Sig1 = "Green"
            P1 = 1
        elif(sortedcar[1]=='A'):
            Sig1 = "Orange"  
            P1 = 2  
        elif(sortedcar[2]=='A'):
            Sig1 = "Red"  
            P1 = 3  
        elif(sortedcar[3]=='A'):
            Sig1 = "Red"  
            P1 = 4 

        if(sortedcar[0]=='B'):
            Sig2 = "Green"
            P2 = 1
        elif(sortedcar[1]=='B'):
            Sig2 = "Orange"  
            P2 = 2  
        elif(sortedcar[2]=='B'):
            Sig2 = "Red"  
            P2 = 3  
        elif(sortedcar[3]=='B'):
            Sig2 = "Red"  
            P2 = 4 

        if(sortedcar[0]=='C'):
            Sig3 = "Green"
            P3 = 1
        elif(sortedcar[1]=='C'):
            Sig3 = "Orange"  
            P3 = 2  
        elif(sortedcar[2]=='C'):
            Sig3 = "Red"  
            P3 = 3  
        elif(sortedcar[3]=='C'):
            Sig3 = "Red"  
            P3 = 4 

        if(sortedcar[0]=='D'):
            Sig4 = "Green"
            P4 = 1
        elif(sortedcar[1]=='D'):
            Sig4 = "Orange"  
            P4 = 2  
        elif(sortedcar[2]=='D'):
            Sig4 = "Red"  
            P4 = 3  
        elif(sortedcar[3]=='D'):
            Sig4 = "Red"  
            P4 = 4                                                                    
       
        for (x,y,w,h) in cars1:
            print(x)
        
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
            if(P1 == 2):
                color = O
            elif(P1 == 1):
                color = G
            else:
                color = R            
        
            #cv2.imshow('video2', frames)
            cv2.putText(img1,"Cars:"+ str(total_cars1),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv2.circle(img1,(50,20),20,color,-1)
            cv2.imwrite(os.path.join("static/images/","1.jpg"),img1)

        for (x,y,w,h) in cars2:
            print(x)
        
            cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)
            if(P2 == 2):
                color = O
            elif(P2 == 1):
                color = G
            else:
                color = R
        
            #cv2.imshow('video2', frames)
            cv2.putText(img2,"Cars:"+ str(total_cars2),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv2.circle(img2,(50,20),20,color,-1)
            cv2.imwrite(os.path.join("static/images/","2.jpg"),img2)

        for (x,y,w,h) in cars3:
            print(x)
        
            cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,255),2)
            if(P3 == 2):
                color = O
            elif(P3 == 1):
                color = G
            else:
                color = R            
        
            #cv2.imshow('video2', frames)
            cv2.putText(img3,"Cars:"+ str(total_cars3),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv2.circle(img3,(50,20),20,color,-1)
            cv2.imwrite(os.path.join("static/images/","3.jpg"),img3)

        for (x,y,w,h) in cars4:
            print(x)
        
            cv2.rectangle(img4,(x,y),(x+w,y+h),(0,0,255),2)
            if(P4 == 2):
                color = O
            elif(P4 == 1):
                color = G
            else:
                color = R            
        
            #cv2.imshow('video2', frames)
            cv2.putText(img4,"Cars:"+ str(total_cars4),(200,20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
            cv2.circle(img4,(50,20),20,color,-1)
            cv2.imwrite(os.path.join("static/images/","4.jpg"),img4) 

        return render_template('traffic.html',P1=P1,P2=P2,P3=P3,P4=P4,T1=T1,T2=T2,T3=T3,T4=T4,Sig1=Sig1,Sig2=Sig2,Sig3=Sig3,Sig4=Sig4,total_cars1=total_cars1,total_cars2=total_cars2,total_cars3=total_cars3,total_cars4=total_cars4)
    return render_template('traffic.html')

@app.route('/video_stream')
def video_stream():
     scen = session.get('scen',None)
     print(scen)
     return Response(get_frame(scen),mimetype='multipart/x-mixed-replace; boundary=frame')
     #return 0     

"""
@app.route('/video_stream2')
def video_stream2():
     scen = session.get('scen',None)
     print(scen)
     return Response(get_frame2(scen),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_stream3')
def video_stream3():
     scen = session.get('scen',None)
     print(scen)
     return Response(get_frame3(scen),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_stream4')
def video_stream4():
     scen = session.get('scen',None)
     print(scen)
     return Response(get_frame4(scen),mimetype='multipart/x-mixed-replace; boundary=frame')
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
