import numpy as np
import cv2
from single_colour_locate_HSV import *
from closest_point import *
import time

cap = cv2.VideoCapture(0)

total_frames: int = 0
processing_time: float = 0
total_time: float = 0
scale_percent = 60

retval, img = cap.read()

width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

blank = np.zeros(img.shape, dtype="uint8")

prev = ()

# out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (2*dim[0],dim[1]))

while True:

	retval, img = cap.read()

	if retval:
		time1 = time.process_time()

		img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
		img = cv2.GaussianBlur(img, (3,3), 1.4)


		cl1 = locate_with_colour(img,r_cl)
		# cl2 = locate_with_colour(img,"r")

		# val = closest_point_pair(cl1[2],cl2[2])

		# if val==-1 or val[2]>30:
		# 	print("At least one list is empty")
		# else:
		# 	centre = (int((val[0][0]+val[1][0])/2), int((val[0][1]+val[1][1])/2))
		# 	cv2.circle(blank, centre, 4, (255,255,255), -1)
		# 	print(centre)
		# 	if len(prev)!=0:
		# 		cv2.line(blank, centre, prev, (255,0,255), 2)
		# 	prev = centre

		time2 = time.process_time() - time1

		# if cl1!=-1 and cl1!=-1:
		# vid = np.concatenate((cv2.bitwise_or(cl1[0],cl2[0]),blank), axis=1)
		# cv2.imshow("output",vid)
		cv2.imshow("img",cl1[0])
		cv2.imshow("mask",cl1[1])
		# out.write(vid)
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
		time3 = time.process_time() - time1
		total_frames+=1
		processing_time+=time2
		total_time+=time3

	else:
		break

print("Frames Processed: "+str(total_frames))
print("Average Processing FPS: "+'{0:.2f}'.format(total_frames/processing_time))
print("Average FPS: "+'{0:.2f}'.format(total_frames/total_time))
cap.release()
# out.release()
cv2.destroyAllWindows()
exit()
