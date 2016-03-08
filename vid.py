import numpy as np
import cv2

cap = cv2.VideoCapture('mmsh://sv04msmedia2.dot.ca.gov/D5-Los-Osos-Valley-Rd-at-101?MSWMExt=.asf')

while(cap.isOpened()):
	ret, frame = cap.read()
	cv2.imshow('vid', frame)
	if cv2.waitKey(120) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
