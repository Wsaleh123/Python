import cv2
import numpy as np


img = cv2.imread("IMG_0357.jpg", 0)

first_frame = None

video = cv2.VideoCapture(0)


while True:
	check, frame = video.read()
	cv2.imshow("Color Frame", frame)
	
	print(cv2.subtract(img, frame))
	
	
	key=cv2.waitKey(1)
	if key == ord('q'):
		break


