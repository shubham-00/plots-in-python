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

Ys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Zs = [5, 6, 2, 3, 13, 4, 1, 2, 4, 8]
Xs = [2, 3, 3, 3, 5, 7, 9, 11, 10, 15]
# Created more arrays as other dataset

ax.scatter(X, Y, Z, color = "blue", marker = "s")	# Instead of plot(), because we want to scatter.
													# marker = "s" or try o, ., p, h, ^, ...

ax.scatter(Xs, Ys, Zs, color = "red", marker = "h")

ax.set_title("Multiple Datasets")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
# Created labels for all three axes

plt.show()
