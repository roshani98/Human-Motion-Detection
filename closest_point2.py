import sys
import math

def dist(a, b):
	return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2))

def closest_point_pair(s1,s2):
	if len(s1)==0 or len(s2)==0:
		return -1

	f1 = 0
	f2 = 0
	current_min = sys.maxsize

	for p1 in s1:
		for p2 in s2:
			if dist(p1, p2)<current_min:
				current_min = dist(p1, p2)
				f1 = p1
				f2 = p2
	return f1, f2, current_min
