import numpy as np
import cv2

videosrc = 'mmsh://sv04msmedia2.dot.ca.gov/D5-Los-Osos-Valley-Rd-at-101?MSWMExt=.asf'
videosrc = 'vid1.avi'
cap = cv2.VideoCapture(videosrc)


while(cap.isOpened()):
	ret, frame = cap.read()
	if ret:
		cv2.imshow('vid', frame)
	else:
		print 'oh no'
		break
	if cv2.waitKey(67) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
