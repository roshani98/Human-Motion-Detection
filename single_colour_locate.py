import numpy as np
import cv2
import imutils


# SINCE OPENCV FOLLOWES BGR FORMAT
HIGH: int = 255
LOW: int = 0

r = (LOW, LOW, HIGH)
R = np.array(r, dtype="uint8")

g = (LOW, HIGH, LOW)
G = np.array(g, dtype="uint8")

b = (HIGH, LOW, LOW)
B = np.array(b, dtype="uint8")

c = (HIGH, HIGH, LOW)
C = np.array(c, dtype="uint8")

m = (HIGH, LOW, HIGH)
M = np.array(m, dtype="uint8")

y = (LOW, HIGH, HIGH)
Y = np.array(y, dtype="uint8")

bl = (LOW, LOW, LOW)
BL = np.array(bl, dtype="uint8")

w = (HIGH, HIGH, HIGH)
W = np.array(w, dtype="uint8")


def locate_with_colour(img, colour, UL=(200,100)):

	# HOW TO:
	
	# PASS IMAGE THAT CONTAINS A SQUARE TRACKER, AN IDEAL COLOUR
	# SUCH AS [0,255,255] or [0,0,255] etc., BUT NOT BLACK, UPPER
	# THRESHOLD FOR MINIMUM POSITIVE CHANNEL VALUE AND
	# LOWER THRESHOLD FOR.MAXIMUM NEGATIVE CHANNEL VALUE.

	# RETURN VALUE IS A LIST OF ALL THE LOCATIONS AND SIZES
	# OF TRACKERS FOUND OF THE SAME COLOUR BASED ON UPPER AND LOWER.

	c_0 = colour[0]
	c_1 = colour[1]
	c_2 = colour[2]

	UPPER = UL[0]
	LOWER = UL[1]

	tracker_locations = []
	if not(c_0 or c_1 or c_2):
		return tracker_locations
	
	shape = img.shape

	# CREATE MASK ACCORDING TO THE CHOICE
	mask_temp = np.zeros(shape, dtype="uint8")
	for i in range(0, shape[0]):
		for j in range(0, shape[1]):
			# CREATE MASK
			if c_0 and not(c_1) and not(c_2):
				if img[i][j][0] > UPPER and img[i][j][1] < LOWER and img[i][j][2] < LOWER:
					mask_temp[i][j] = B
			if c_1 and not(c_2) and not(c_0):
				if img[i][j][1] > UPPER and img[i][j][2] < LOWER and img[i][j][0] < LOWER:
					mask_temp[i][j] = G
			if c_2 and not(c_0) and not(c_1):
				if img[i][j][2] > UPPER and img[i][j][0] < LOWER and img[i][j][1] < LOWER:
					mask_temp[i][j] = R
			if c_0 and c_1 and not(c_2):
				if img[i][j][0] > UPPER and img[i][j][1] > UPPER and img[i][j][2] < LOWER:
					mask_temp[i][j] = C
			if c_1 and c_0 and not(c_2):
				if img[i][j][0] > UPPER and img[i][j][2] > UPPER and img[i][j][1] < LOWER:
					mask_temp[i][j] = M
			if c_2 and c_1 and not(c_0):
				if img[i][j][2] > UPPER and img[i][j][1] > UPPER and img[i][j][0] < LOWER:
					mask_temp[i][j] = Y
			if c_0 and c_1 and c_2:
				if img[i][j][0] > UPPER and img[i][j][1] > UPPER and img[i][j][2] > UPPER:
					mask_temp[i][j] = W

	# FIND CONTOURS FROM INTERESTING CHANNEL
	mask = mask_temp[:, :, 0]
	channel = 0;
	for k in range(0,3):
		if colour[k]:
			channel = k
			mask = mask_temp[:,:,k]
			break

	# cv2.imshow("mask",mask)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	if len(cnts) > 0: # IF YOU FIND CONTOURS
		final_contours = []

		for c in cnts:
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.02 * peri, True)

			if len(approx) == 4 and peri > 10: # AND ANY IF THEM HAS 4 SIDES AND
												# LENGTH MORE THAN 10
				final_contours.append(approx)

		if len(final_contours) > 0:
			for a in final_contours:
				x = img.shape[0]
				y = img.shape[1]
				l = 0
				h = 0
				for b in a:
					if b[0][0]<x:
						x = b[0][0]
					if b[0][1]<y:
						y = b[0][1]
					if b[0][0]>=l:
						l = b[0][0]
					if b[0][1]>=h:
						h = b[0][1]
				l = l-x
				h = h-y
				# cv2.rectangle(img, (x,l), (y,h), (0,0,0), 5)
				tracker_locations.append((x+l/2,y+h/2))

	return tracker_locations
