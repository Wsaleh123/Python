import cv2
import glob2

filenames = glob2.glob("*.jpg")

def resize(filename):
	img = cv2.imread(filename,0)
	cv2.imshow("Hey", img)
	cv2.waitKey(0)
	img = cv2.imread(filename, 1)
	resized_image=cv2.resize(img, (100,100))
	cv2.imwrite("resized" +filename, resized_image)

for filename in filenames:
	resize(filename)