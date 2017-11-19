import cv2, time, pandas
from datetime import datetime
from difflib import SequenceMatcher

first_frame = None

video = cv2.VideoCapture(0)

while True:
	check, frame = video.read()
	cv2.imshow("Color Frame", frame)
	
	if first_frame is None:
		first_frame = frame
	else:
		pass
	
	match = SequenceMatcher(None, str(first_frame), str(frame)).ratio()
	print(match)
	
	key=cv2.waitKey(1)
	if key == ord('q'):
		break

