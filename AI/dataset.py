import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#Load the Iris dataset

iris=load_iris()
X,y=iris.data,iris.target

#Split the data into data training and testing sets

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#Create and gtrain the Random Forest Classifier

rf_classifier=RandomForestClassifier(n_estimators=100,random_state=42)
rf_classifier.fit(X_train,y_train)

#Make predictions on the test set~

y_pred=rf_classifier.predict(X_test)

#Calculate and display the accuracy

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)

#Display the classification report

class_names=iris.target_names
print("Classification Report:")
print(classification_report(y_test,y_pred,target_names=class_names))

#Display the confusion matrix
confusion_mat=confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(confusion_mat)