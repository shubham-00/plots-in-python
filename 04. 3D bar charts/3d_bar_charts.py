'''
Shubham Patel
Github: github.com/shubham-00
LinkedIn: https://www.linkedin.com/in/srpatel980/
Contact for more.
'''


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()	# Creating an empty figure
ax1 = fig.add_subplot(111, projection = "3d")	# Added an empty 3d plot
												# 111 means 1*1 grid and 1st subplot
												# abc means a*b grid and cth subplot

# Let, that viewer is viewing on Z axis, so X axis is width, Y axis is the depth, and Z axis is the height of the bar.
xpos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	# So, all the bars are standing in a line, each starting from 1 to 10.
ypos = [2, 3, 4, 5, 1, 6, 2, 1, 7, 2]	# This is the depth of the bar. Each bar is starting from this list.
zpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	# Height is starting from 0 for each bar.
# Created three arrays (lists) for starting position

dx = np.ones(10)	# now dx containes 10 elements which are "1" (numeric)
					# So, width of each bar is 1 unit.
dy = np.ones(10)	# So, depth of each bar is 1 unit.
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	# Height of each bar is like this array. Starting from 1 to 10.

ax1.set_title("3D Bars")
ax1.set_xlabel("X axis")
ax1.set_ylabel("Y axis")
ax1.set_zlabel("Z axis")
# Created labels for all three axes

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color = "#FF0000")	# This is how we plot 3d bars.

plt.show()


'''
Shubham Patel
Github: github.com/shubham-00
LinkedIn: https://www.linkedin.com/in/srpatel980/
Contact for more.
'''
