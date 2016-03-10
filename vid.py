import numpy as np
import cv2

cap = cv2.VideoCapture('mmsh://sv04msmedia2.dot.ca.gov/D5-Los-Osos-Valley-Rd-at-101?MSWMExt=.asf')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter("output.avi", fourcc, 15, (640, 480))

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret:
		cv2.imshow('vid', frame)
		video_writer.write(frame)
	else:
		print 'oh no'
		break
	if cv2.waitKey(67) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
