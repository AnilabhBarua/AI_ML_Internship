#3D Scatter Plot
#3D scatter plot is one of the most frequently used threedimensional graphs for comparing the three characteristics of a given dataset.
#The 3D plot is a collection of scatter plots created from the sets of (x, y, z) dataset.
#It is particularly useful for investigating the relationships among the variables.
#Hence, up to four variables (three numeric and one categorical) may be displayed on a single graph

#Program 6: Displaying 3D Scatter Plot
import matplotlib.pyplot as plt
import numpy as np
# Create the fixed data values and colors
x1 = np.array([5, 7, 6, 4, 5])
y1 = np.array([9, 8, 6, 9, 7])
z1 = np.array([1, 2, 3, 1, 2])
color1 = 'red'
x2 = np.array([1, 3, 4, 6, 4])
y2 = np.array([1, 3, 4, 6, 5])
z2 = np.array([5, 3, 5, 2, 1])
color2 = 'green'
x3 = np.array([10, 8, 9, 8, 9])
y3 = np.array([9, 7, 8, 9, 10])
z3 = np.array([8, 9, 7, 8, 10])
color3 = 'blue'
# Create the figure and the 3D axes
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# Plot the scatter plots with the given fixed data values and color specifications
ax.scatter(x1, y1, z1, color=color1)
ax.scatter(x2, y2, z2, color=color2)
ax.scatter(x3, y3, z3, color=color3)
# Set the labels for each axis
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# Show the plot
plt.show()
