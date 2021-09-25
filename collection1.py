import numpy as np
import cv2
from single_colour_locate_HSV import *
# from closest_point import *
import closest_point2
import time

def collect(f_in, disp_var=0):
	cap = cv2.VideoCapture(f_in)

	total_frames: int = 0
	# processing_time: float = 0
	total_time: float = 0
	scale_percent = 100

	retval, img = cap.read()
	width = int(img.shape[1] * scale_percent/100)
	height = int(img.shape[0] * scale_percent/100)
	dim = (width,height)
	img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

	colour = (r_cl, y_cl, g_cl, c_cl, b_cl, m_cl)
	colour_positions = dict()
	body_points = {"point":(g_cl, c_cl, [])}

	while True:
		# print("reading\n")
		c1 = 0
		c2 = 0

		retval, img = cap.read()

		if retval:
			time1 = time.process_time()

			img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
			img = cv2.GaussianBlur(img, (3,3), 1.4)

			for i in colour:
				colour_positions[i] = locate_with_colour(img, i)

			for i in body_points:
				c1 = body_points[i][0]
				c2 = body_points[i][1]

				closest_point = closest_point2.closest_point_pair(colour_positions[c1][2], colour_positions[c2][2])
				if closest_point != -1:
					if closest_point[2] < 40:
						centre = (int((closest_point[0][0]+closest_point[1][0])/2),int((closest_point[0][1]+closest_point[1][1])/2))
						body_points[i][2].append((centre, total_frames))
					else:
						body_points[i][2].append(((-1, -1), total_frames))
				else:
					body_points[i][2].append(((-1, -1), total_frames))

			# time2 = time.process_time() - time1

			time3 = time.process_time() - time1

			# k = cv2.waitKey(5) & 0xFF
			# if k == 27:
			# 	break

			total_frames+=1
			# processing_time+=time2
			total_time+=time3

		else:
			break

		colour_positions.clear()

	cap.release()

	cv2.destroyAllWindows()

	if disp_var:
		print("Processing Information:")
		print("\tStream Size: "+str(dim))
		print("\tFrames Processed: "+str(total_frames))
		# print("\tProcessing Time (seconds): "+'{0:.2f}'.format(processing_time))
		print("\tTotal Time (seconds): "+'{0:.2f}'.format(total_time))
		# print("\tProcessing Time per Frame (seconds): "+'{0:.2f}'.format(processing_time/total_frames))
		print("\tTotal Time per Frame(seconds): "+'{0:.2f}'.format(total_time/total_frames))
		# print("\tAverage Processing FPS: "+'{0:.2f}'.format(total_frames/processing_time))
		print("\tAverage FPS: "+'{0:.2f}'.format(total_frames/total_time))

	return body_points, total_frames
