#KNN Classification
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Generate sample dataset
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2, 
random_state=1, n_clusters_per_class=1)
# Display first five values of X and y
print("First five values of X:")
print(X[:5])
print()
print("First five values of y:")
print(y[:5])
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# Fit KNN classifier to training set
k = 5
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X_train, y_train)
# Predict labels for testing set
y_pred = clf.predict(X_test)
# Print accuracy score
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
# Visualize decision boundary
xx, yy = np.meshgrid(np.linspace(-4, 4, 500), np.linspace(-4, 4, 500))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
plt.show()
