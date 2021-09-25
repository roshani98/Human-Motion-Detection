import numpy as np
import cv2
from single_colour_locate_HSV import *
# from closest_point import *
import closest_point2
import time

cap = cv2.VideoCapture("videos2/sample5.mov")

total_frames: int = 0
processing_time: float = 0
total_time: float = 0
scale_percent = 100

retval, img = cap.read()
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)
dim = (width,height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

canvas = np.zeros(img.shape, dtype="uint8")
current_img = np.zeros(img.shape, dtype="uint8")

filename = "output-sample5.avi"
# out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M','J','P','G'), 5, (2*dim[0],dim[1]))

colour = (r_cl, y_cl, g_cl, c_cl, b_cl, m_cl)
colour_positions = dict()
body_points = {"left_wrist":(g_cl, c_cl, [], []), "left_elbow":(y_cl, c_cl, [], []), "left_shoulder":(y_cl, b_cl, [], [])}
# explanation for body_points data structure:
# key = point name
# assume val = body_points[key]
# val[0] = first colour = line colour
# val[1] = second colour = circle colour
# val[2] = list of centres
# val[3] = previous x and y. Once used, they will be cleared

# DONT ASK ME ABOUT THIS AFTER A MONTH.
# I WON"T REMEMBER HOW A SINGLE THING WORKS.

while True:
	c1 = 0
	c2 = 0

	retval, img = cap.read()

	if retval:
		time1 = time.process_time()

		img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
		img = cv2.GaussianBlur(img, (3,3), 1.4)
		current_img = img

		for i in colour:
			colour_positions[i] = locate_with_colour(img, i)
			current_img = cv2.bitwise_and(current_img, colour_positions[i][0])

		for i in body_points:
			c1 = body_points[i][0]
			c2 = body_points[i][1]

			closest_point = closest_point2.closest_point_pair(colour_positions[c1][2], colour_positions[c2][2])
			if closest_point != -1:
				if closest_point[2] < 40:
					centre = (int((closest_point[0][0]+closest_point[1][0])/2),int((closest_point[0][1]+closest_point[1][1])/2))
					body_points[i][2].append((centre, total_frames))
					# cv2.circle(canvas, centre, 5, body_points[i][1], -1)
					if len(body_points[i][3]) > 0:
						cv2.line(canvas, centre, (body_points[i][3][0], body_points[i][3][1]), body_points[i][0], 2)
					body_points[i][3].clear()
					body_points[i][3].append(centre[0])
					body_points[i][3].append(centre[1])
				else:
					body_points[i][2].append((None, total_frames))
			else:
				body_points[i][2].append((None, total_frames))

		time2 = time.process_time() - time1

		cv2.putText(canvas,str(total_frames),(dim[0]-100, dim[1]-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

		output_img = np.concatenate((current_img, canvas), axis=1)
		# cv2.imshow("output", output_img)
		# out.write(output_img)

		cv2.putText(canvas,str(total_frames),(dim[0]-100, dim[1]-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

		time3 = time.process_time() - time1

		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break

		total_frames+=1
		processing_time+=time2
		total_time+=time3

	else:
		break

	colour_positions.clear()

cap.release()
# out.release()
cv2.destroyAllWindows()

# canvas = cv2.flip(canvas, 0)
cv2.imwrite("output_img2.png", canvas)

print("Textual Data:")
print(body_points)
print("\nProcessing Information:")
print("\tStream Size: "+str(dim))
print("\tFrames Processed: "+str(total_frames))
print("\tProcessing Time (seconds): "+'{0:.2f}'.format(processing_time))
print("\tTotal Time (seconds): "+'{0:.2f}'.format(total_time))
print("\tProcessing Time per Frame (seconds): "+'{0:.2f}'.format(processing_time/total_frames))
print("\tTotal Time per Frame(seconds): "+'{0:.2f}'.format(total_time/total_frames))
print("\tAverage Processing FPS: "+'{0:.2f}'.format(total_frames/processing_time))
print("\tAverage FPS: "+'{0:.2f}'.format(total_frames/total_time))
exit()
