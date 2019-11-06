from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()	# Creates an empty figure (plot)
ax = fig.add_subplot(111, projection = "3d")	# Adds an empty 3d plot
											# 111 means 1*1 grid and 1st subplot
											# abc means a*b grid and cth subplot
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [5, 6, 2, 3, 13, 4, 1, 2, 4, 8]
Z = [2, 3, 3, 3, 5, 7, 9, 11, 10, 15]
# Created three arrays

ax.scatter(X, Y, Z, color = "blue")	# Instead of plot(), because we want to scatter.

ax.set_title("3D Scattering")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

plt.show()
