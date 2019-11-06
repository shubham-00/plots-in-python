'''
Shubham Patel
Github: github.com/shubham-00
LinkedIn: https://www.linkedin.com/in/srpatel980/
Contact for more.
'''


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()	# Creating an empty figure
ax = fig.add_subplot(111, projection = "3d")	# Added an empty 3d plot
												# 111 means 1*1 grid and 1st subplot
												# abc means a*b grid and cth subplot

x, y, z = axes3d.get_test_data(delta = 0.1)
ax.plot_wireframe(x, y, z, rstride = 3, cstride = 3)
# rstride, cstride => how often we draw a line (row, colunm)
# delta => how often we compute a line

ax.set_title("3D Plane")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

#print(x, y, z)

plt.show()


'''
Shubham Patel
Github: github.com/shubham-00
LinkedIn: https://www.linkedin.com/in/srpatel980/
Contact for more.
'''
