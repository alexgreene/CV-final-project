from urllib2 import urlopen
import urllib
import time

import numpy
import cv2

# image 1 --> temporary image store
# image 2 --> captured image
# image 3 --> background image

def grab_traffic_cam(url, filename):
    urllib.urlretrieve(url, filename)

def update_snapshot(): 
    # http://webcam.mta.info/btimg/172.28.201.8/1/image.jpg <-- triborough bridge tollbooth
    # http://207.251.86.238/cctv720.jpg 

    print "Collecting Image ..."
    grab_traffic_cam('http://207.251.86.238/cctv794.jpg', 'nyc_001.jpg')
    print time.ctime()

    while images_are_equal(1, 2) == True:
        print "No image difference. Reloading..."
        update_resource()

    cv2.imwrite('nyc_002.jpg', cv2.imread('nyc_001.jpg'))
    print "Image updated."


def images_are_equal(a, b):
    a = cv2.imread("nyc_00" + str(a) + ".jpg")
    b = cv2.imread("nyc_00" + str(b) + ".jpg")
    return a.shape == b.shape and not( numpy.bitwise_xor(a, b).any() )


def get_resources(a, b):
    a = cv2.imread("nyc_00" + str(a) + ".jpg")
    b = cv2.imread("nyc_00" + str(b) + ".jpg")

    return (a, b)


def diff_images(a, b):
    # diff the images
    a = cv2.cvtColor(a, cv2.cv.CV_RGB2GRAY);
    #(T, a) = cv2.threshold(a, 127.0, 255.0, cv2.THRESH_BINARY);

    b = cv2.cvtColor(b, cv2.cv.CV_RGB2GRAY);
    #(T, b) = cv2.threshold(b, 127.0, 255.0, cv2.THRESH_BINARY);

    diff = cv2.subtract(a, b)

    # create image mask
    mask = cv2.imread('nyc_mask.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    (T, mask) = cv2.threshold(mask, 230.0, 255.0, cv2.THRESH_BINARY);

    # mask original image
    diff = cv2.bitwise_and(diff, diff, mask = mask)

    #display result
    cv2.imshow("result", diff)

    # return inverted diff'ed image
    return (255-diff)


def detect_vehicles(a, diff):

    params = cv2.SimpleBlobDetector_Params()
          
    # set the minimum area for a detected blob
    params.filterByArea = True
    params.minArea = 10
     
    blobdet = cv2.SimpleBlobDetector(params)
    vehicles = blobdet.detect(diff)

    print str( len(vehicles) ) + " vehicles detected"

    # displays the detection points on top of original image
    blobs = cv2.drawKeypoints(a, vehicles, numpy.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # displays the detection points on top of diff'ed image
    blobs2 = cv2.drawKeypoints(diff, vehicles, numpy.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
     
    # Show keypoints
    cv2.imshow("vehicles", blobs)
    cv2.imshow("vehicles (diff)", blobs2)
    cv2.waitKey()


#RUN 
update_snapshot()
(a, b) = get_resources(2, 3) 
ret_diff = diff_images(a, b) 
detect_vehicles(a, ret_diff)


