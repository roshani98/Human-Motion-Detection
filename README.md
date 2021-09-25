# Marker Detection

There are four python files that are used:

  - single_colour_locate_HSV.py
  - closest_point.py
  - temp.py
  - old-temp.py

# How to

  - Put all the files in the same directory
  - Install reuirements via running "pip3 install -r requirements.txt"
  - run temp.py py by putting "python3 temp.py" or "python3 old-temp.py"
  - temp.py is for running the actual experimenting, while the other one is for internal checking.

# What you should see

 - A video stream of your webcam after processing, with tracked outputs on the right side. Something like this:
![](output_gif.gif)

# What you can do

  - You can generate your own sample images via opencv and its drawing functions to make your own trackers
  - You can change the colours in temp.py to play around with your own perceptions.
  - You can tweak the values of colours from single_colour_locate_HSV.py to generate useful data from real images

# Publication Link
[Inverse Kinematics Based Computational Framework for Robot Manipulation Inspired by Human Movements](https://link.springer.com/chapter/10.1007%2F978-981-15-8061-1_17)
