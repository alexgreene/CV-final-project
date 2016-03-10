# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
#video_src = 'dataset/output.avi'
video_src = 'mmsh://sv04msmedia2.dot.ca.gov/D5-Los-Osos-Valley-Rd-at-101?MSWMExt=.asf'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
mask = cv2.imread('mask.png')
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    masked_data = cv2.bitwise_and(gray, mask)
    
    
    cars = car_cascade.detectMultiScale(masked_data, 1.1, 2, 0, (30,30), (100,100))

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)      
    
    cv2.imshow('LOVR 101 Live Feed', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
