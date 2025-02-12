#Decision Tree Classification
# The code first loads the Iris dataset and selects the first and third feature for
# visualization. 
# A Decision Tree classifier is trained on the data with a maximum depth of 2.
# The decision boundary is plotted by generating a mesh grid over the feature space
# and predicting the class labels for each point in the grid using the trained classifier. 
# The decision boundary is shown as a contour plot, where each color represents a
# different class label.
# The training points are plotted on top of the decision boundary with different colors
# representing different class labels. 
# Finally, the decision tree is visualized using the plot_tree function.
# The filled=True argument is used to color the nodes based on their majority class.

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np
#load dataset
iris=load_iris()
X=iris.data[:,[o,2]]# select the first and third feature for visualization 
Y=iris.target
# Train a Decision Tree classifier
clf = DecisionTreeClassifier(max_depth=2)
clf.fit(X, y)
# Plot the decision boundary
plt.figure(figsize=(8, 6))
plot_step = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Petal length')
# Plot the decision tree
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True)
plt.show()
