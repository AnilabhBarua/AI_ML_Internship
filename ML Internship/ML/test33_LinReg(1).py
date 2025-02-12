#linear regression
#import the libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
# import dataset
dataset =pd.read_csv ("Salary_Data.csv")
#split into training and testing dataset
from sklearn.model_selection import train_test_split
X=dataset.iloc[:,[0]].values #get YearsExp column
y=dataset.iloc[:,[1]].values #get Salary column
#1/3 of the data for testing
X_train,X_test,y_train,y_test=train_test_split (X,y,test_size=0.33, random_state=0)
#linear regression
from sklearn.linear_model import LinearRegression
regressor=LinearRegression() #Create linear regression object
regressor.fit(X_train,y_train)# Train the model using the training sets
y_pred = regressor.predict(X_test)# Make predictions using the testing set
# If variance score is 1, it is perfect prediction
print('\n\n Variance S core: %.2f' % r2_score(y_test, y_pred))
#plot
plt.scatter(X_train,y_train, color="red") #data point
plt.plot(X_train, regressor.predict(X_train), color="blue")#regression line
plt.title("Salary vs Years of Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
plt.scatter(X_test,y_test, color="red") #data point
plt.plot(X_test , regressor.predict(X_test ), color="blue") #regression line
plt.title("Salary vs Years of Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
#predict
y_pred= regressor.predict ([[13.5]])
y_pred= np.round(y_pred,2)
print("\n\n Linear Regression n Given new X Value = 13.5")
print(" Predicted Y value = ",y_pred)
