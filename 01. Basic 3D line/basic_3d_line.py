'''
Shubham Patel
Github: github.com/shubham-00
LinkedIn: https://www.linkedin.com/in/srpatel980/
Contact for more.
'''


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()	# Figure(640x480)	||	Creates an empty figure
ax = fig.add_subplot(111, projection = "3d")	# Adds an enpty 3d plot
												# 111 means 1*1 grid and 1st subplot
												# abc means a*b grid and cth subplot

X, Y, Z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6, 3, 13, 4, 1, 2, 4, 8, 10], [2, 3, 3, 3, 5, 7, 9, 11, 9, 10]	# Creating three arrays (lists actually)
plt.plot(X, Y, Z)	# Plots in 3d

ax.set_title("Basic 3D Line")

plt.show()	# Actually plots on the screen


'''
Shubham Patel
Github: github.com/shubham-00
LinkedIn: https://www.linkedin.com/in/srpatel980/
Contact for more.
'''
