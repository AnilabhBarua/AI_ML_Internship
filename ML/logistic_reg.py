# logistic regression
# import the libraries
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd

# import dataset
dataset = pd.read_csv("User_Data.csv")
print(dataset)

# split into training and testing dataset
from sklearn.model_selection import train_test_split  
X = dataset.iloc[:, [2, 3]].values # get Age column  
y = dataset.iloc[:, 4].values # get EstimatedSalary column
# 1/3 of the data for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, 
random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler  
sc_x = StandardScaler() 
X_train=sc_x.fit_transform(X_train)
X_test=sc_x.transform(X_test)

#Apply Logistic Regression
from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression(random_state = 0) 
classifier.fit(X_train, y_train) 

y_pred = classifier.predict(X_test) # Make predictions using the testing set
#Evaluation Metric
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test, y_pred) 
print("Confusion Matrix : \n", cm) 

#Performance Accuracy
from sklearn.metrics import accuracy_score 
print ("Accuracy : ", accuracy_score(y_test, y_pred)) 

#Display Graphical Result
from matplotlib.colors import ListedColormap 
X_set, y_set = X_test, y_test 
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1,  
                               stop = X_set[:, 0].max() + 1, step = 0.01), 
                     np.arange(start = X_set[:, 1].min() - 1,  
                               stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green'))) 
plt.xlim(X1.min(), X1.max()) 
plt.ylim(X2.min(), X2.max()) 

for i, j in enumerate(np.unique(y_set)): 
  plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],c = ListedColormap(('red', 'green'))(i), label = j) 
plt.title('Classifier (Test set)') 
plt.xlabel('Age') 
plt.ylabel('Estimated Salary') 
plt.legend() 
plt.show() 
