import numpy as np
import cv2
import imutils


HIGH: int = 255
LOW: int = 0

r_cl = (LOW, LOW, HIGH)
lower_red_1 = np.array([0,50,50])
upper_red_1 = np.array([10,255,255])
lower_red_2 = np.array([170,50,50])
upper_red_2 = np.array([179,255,255])

y_cl = (LOW, HIGH, HIGH)
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([40, 255, 255])

g_cl = (LOW, HIGH, LOW)
lower_green = np.array([50, 50, 50])
upper_green = np.array([70, 255, 255])

c_cl = (HIGH, HIGH, LOW)
lower_cyan = np.array([80, 50, 50])
upper_cyan = np.array([100, 255, 255])

b_cl = (HIGH, LOW, LOW)
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

m_cl = (HIGH, LOW, HIGH)
lower_magenta = np.array([140, 50, 50])
upper_magenta = np.array([160, 255, 255])


def locate_with_colour(img, colour):

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	if colour==r_cl:
		mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
		mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
		mask = cv2.bitwise_or(mask_1, mask_2)
		# colour2 = r_cl
	elif colour==y_cl:
		mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
		# colour2 = y_cl
	elif colour==g_cl:
		mask = cv2.inRange(hsv, lower_green, upper_green)
		# colour2 = g_cl
	elif colour==c_cl:
		mask = cv2.inRange(hsv, lower_cyan, upper_cyan)
		# colour2 = c_cl
	elif colour==b_cl:
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		# colour2 = b_cl
	elif colour==m_cl:
		mask = cv2.inRange(hsv, lower_magenta, upper_magenta)
		# colour2 = m_cl
	else:
		return -1

	tracker_locations = []
	cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	if len(cnts) > 0:
		final_contours = []

		for c in cnts:
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.1 * peri, True)

			if len(approx) == 4 and peri > 20:
				(x,y,h,w) = cv2.boundingRect(approx)
				ratio = w/float(h)

				if h >= 7 and w >= 7 and h <= 40 and w <= 40 and ratio >= 0.7 and ratio <= 1.4:
					final_contours.append(approx)
					cv2.rectangle(img, (x, y), (x+h, y+w), colour, 5)
					tracker_locations.append((x+h/2, y+w/2))

	return img, mask, tracker_locations
