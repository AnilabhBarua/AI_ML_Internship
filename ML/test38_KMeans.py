# K-Means Clustering
# import the libraries
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
# Example data points
data_points = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [1, 3], [8, 9], [0, 3], [5, 4], [6, 4], 
[3, 3], [2, 8], [2, 6], [7, 7], [6, 2], [8, 4], [4, 8], [9, 6], [3, 7]])
# Creating KMeans instance with 3 clusters
kmeans = KMeans(n_clusters=3)
# Fitting the data points to the KMeans model
kmeans.fit(data_points)
# Getting the cluster labels assigned to each data point
labels = kmeans.labels_
print("\n 3 Cluster Labels Assigned :")
print(np.unique(labels))
# Getting the cluster centers
centers = kmeans.cluster_centers_
print("\n Final 3 Cluster Centroid Data Points :")
print(np.round(centers,2))
# Visualizing the clusters
plt.scatter(data_points[:, 0], data_points[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering')
plt.show()
