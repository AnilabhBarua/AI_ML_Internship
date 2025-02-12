# Fuzzy c-Means Clustering
# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
# Generate random data points
np.random.seed(0)
n_points = 100
n_clusters = 3
data_points = np.random.randn(n_points, 2)
print("\n First 5 Data Points")
print(data_points[0:5])
# Fuzzy c-means clustering
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(data_points.T, n_clusters, 2, error=0.005, 
maxiter=1000, init=None)
# Get the cluster membership values
cluster_membership = np.argmax(u, axis=0)
# Create a figure and axes object
fig, ax = plt.subplots()
# Plotting the data points and clusters
for j in range(n_clusters): 
ax.scatter(data_points[cluster_membership == j, 0], 
data_points[cluster_membership == j, 1], label='Cluster {}'.format(j))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fuzzy c-Means Clustering')
ax.legend()
plt.show()
