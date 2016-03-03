from urllib2 import urlopen
import urllib
import time

import numpy
import cv2

def grab_traffic_cam(url, filename):
    urllib.urlretrieve('http://207.251.86.238/cctv696.jpg', filename)

def update_resources(): 
    print "Updating Images ..."

    for i in range(1, 4): 
        print "Collecting Image " + str(i) + "..."
        grab_traffic_cam('http://207.251.86.238/cctv696.jpg', 'nyc_00' + str(i) + '.png')
        print time.ctime()
        print "... Image " + str(i) + " Collected"

        # wait 4 seconds
        time.sleep(.5)

    print "... Update Complete"

def bg_subtract():
    vc = cv2.VideoCapture("nyc_%3d.png")
    _,f = vc.read()

    avg1 = numpy.float32(f)
    avg2 = numpy.float32(f)
     
    while(1):
        _,f = vc.read()
         
        cv2.accumulateWeighted(f,avg1,0.1)
        cv2.accumulateWeighted(f,avg2,0.01)
         
        res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)
     
        cv2.imshow('img',f)
        cv2.imshow('avg1',res1)
        cv2.imshow('avg2',res2)
        k = cv2.waitKey(20)
     
        if k == 27:
            break
     
    #cv2.destroyAllWindows()
    vc.release()

#RUN 
update_resources() # pictures'A' and 'B' are now in the current directory
bg_subtract() 


