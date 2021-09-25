import collection1
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
import copy
import os
import numpy.random as rand
import json
import ast

vids = ["videos3/A.mov", "videos3/B.mov", "videos3/C.mov", "videos3/D.mov", "videos3/E.mov", "videos3/F.mov", "videos3/G.mov", "videos3/H.mov", "videos3/I.mov"]

mu = 0
sigma = 5
size = 1
dict_2 = {}

for f_in in vids:
	dance_dict = dict()
	temp_dict, total_frames = collection1.collect(f_in)
	for point_name in temp_dict:
		dance_dict[point_name] = temp_dict[point_name][2]

	FINAL_FRAMES = 100

	interpolated_dict = {}
	current = 0
	for frames in dance_dict.values():
		t = frames
		x = []
		y = []
		for i in range(0, len(t)):
			if (t[i][0][0] != -1) and (t[i][0][1] != -1):
				x.append(t[i][0][0])
				y.append(t[i][0][1])

		xnew = []
		ynew = []
		if FINAL_FRAMES < len(x):
			indices = np.linspace(0, len(x)-1, FINAL_FRAMES)
			indices = [int(ind) for ind in indices]
			for i in indices:
				xnew.append(x[i])
				ynew.append(y[i])
		else:
			frames_to_be_added = FINAL_FRAMES - len(x)
			modulo = frames_to_be_added % (len(x) - 1)
			beet_two_pnts = int(frames_to_be_added/(len(x) - 1))

			for i in range(0, len(x)-1):
				if modulo != 0:
					if (x[i] == x[i+1]):
						temp_list = list(np.linspace(x[i], x[i+1], num=3 + beet_two_pnts))[:-1]
						y_temp_list = [y[i]]*(len(temp_list))
						xnew = xnew + temp_list
						ynew = ynew + list(y_temp_list)
					else:
						f = interp1d([x[i],x[i+1]], [y[i],y[i+1]])
						temp_list = list(np.linspace(x[i], x[i+1], num=3 + beet_two_pnts))[:-1]
						xnew = xnew + temp_list
						ynew = ynew + list(f(temp_list))
					modulo = modulo - 1
				else:
					if (x[i] == x[i+1]):
						temp_list = list(np.linspace(x[i], x[i+1], num=2 + beet_two_pnts))[:-1]
						y_temp_list = [y[i]]*(len(temp_list))
						xnew = xnew + temp_list
						ynew = ynew + list(y_temp_list)
					else:
						f = interp1d([x[i],x[i+1]], [y[i],y[i+1]])
						temp_list = list(np.linspace(x[i], x[i+1], num=2 + beet_two_pnts))[:-1]
						xnew = xnew + temp_list
						ynew = ynew + list(f(temp_list))
			xnew.append(x[-1])
			ynew.append(y[-1])

		interp = []
		for index in range(0, len(xnew)):
			interp.append((xnew[index], ynew[index]))

		interpolated_dict[list(dance_dict.keys())[current]] = interp
		current = current + 1

	for key in interpolated_dict:
		temp_list_x = []
		temp_list_y = []
		for point in interpolated_dict[key]:
			temp_list_x.append(point[0])
			temp_list_y.append(point[1])

		max_val = max(temp_list_y)
		for i in range(0, len(temp_list_y)):
			# temp_list_x[i] = temp_list_x[i] - temp_list_x[0]
			temp_list_y[i] = max_val - temp_list_y[i]
			# temp_list_y[i] = temp_list_y[i] - temp_list_y[0]

		new_list = []
		new_list2 = []
		for i in range(0, 30):
			new_list2.append(total_frames)
			for j in range(0, len(temp_list_x)):
				temp_list_x[j] += int(rand.normal(mu, sigma, size))
				temp_list_y[j] += int(rand.normal(mu, sigma, size))
			list_x = gaussian_filter1d(temp_list_x, 2)
			list_y = gaussian_filter1d(temp_list_y, 2)

			for j in range(0, len(temp_list_x)):
				new_list2.append([int(list_x[j]), int(list_y[j])])
			new_list.append(new_list2[:])
			list_x*=0
			list_y*=0
			new_list2*=0

		interpolated_dict[key] = new_list[:]
		temp_list_x*=0
		temp_list_y*=0
		new_list*=0

	dict_2[f_in] = interpolated_dict.copy()
	interpolated_dict.clear()

with open("outfile.json", "w") as json_file:
	json.dump(dict_2, json_file)

exit()
