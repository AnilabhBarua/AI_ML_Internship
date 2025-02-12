# logistic regression
# import the libraries
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Loading dataset
dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(dataset.head())
# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(dataset.iloc[:, :-1],
                                    dataset.iloc[:, -1], test_size=0.3, random_state=0)
# Creating an instance of the logistic regression model
logistic_regression_model = LogisticRegression()
# Training the model on the training data
logistic_regression_model.fit(X_train, y_train)
# Making predictions on the testing data
y_pred = logistic_regression_model.predict(X_test)
# Evaluating the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print('\n Accuracy:', accuracy)
# Calculating and printing the confusion matrix with label names
confusion_mat = confusion_matrix(y_test, y_pred)
class_names = dataset.iloc[:, -1].unique() # Extracting class names from the dataset
confusion_mat_df = pd.DataFrame(confusion_mat, index=class_names, columns=class_names)
sns.heatmap(confusion_mat_df, annot=True, cmap='Blues')
plt.title('Confusion matrix')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()
