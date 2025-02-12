#Python code for data transformation

import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s

#Creating a DataFrame
d = {'C1':[1,3,7,4],'C2':[12,2,7,1],'C3':[22,34,-11,9]}
df2 = pd.DataFrame(d)
print("\n ORIGINAL DATA VALUES")
print("-----------------------")
print(df2)

#Method 1: Rescaling Data
print("\n\n Data Scaled Between 0 to 1")
data_scalar = preprocessing.MinMaxScaler(feature_range = (0,1))

data_scaled = data_scalar.fit_transform(df2)
print("\n Min Max Scaled Data")
print("----------------------")
print(data_scaled.round(2))

#Method 2: Normalization rescales such that sum of each row is 1.
dn = preprocessing.normalize(df2, norm ='l1')
print("\n L1 Normalized Data")
print("---------------------")
print(dn.round(2))

#Method 3: Binarize Data (Make Binary)
data_binarized = preprocessing.Binarizer (threshold=5).transform(df2)
print("\n Binarized Data")
print("-----------------")
print(data_binarized)

#Designing a Bar Diagram

import matplotlib.pyplot as plt
import numpy as np
data = ('Fortran','C','C++','Java','MATLAB','Python')
P = [1, 2, 4, 6, 8, 10]
y = np.arange(len(data))

#Plotting the Bar Graph
plt.bar(y, P, align='center', alpha=0.5, edgecolor = 'black')
plt.xlabel('Programming Language')
plt.ylabel('No. of Usage')
plt.title('Programming Languages Used in Projects')
plt.show()

#Program 3: Displaying Pie Chart

import matplotlib.pyplot as plt
#Data to plot

l = ['Data Science', 'Soft COmputing', 'Cloud Computing', 'Mean Stack']

sizes = [40, 20, 15 ,25] #percentages

#Create pie chart
plt.pie(sizes, labels=1, autopct='%1.1f%%')

#Add title
plt.title('MCA Elective Distribution')

#Show Plot
plt.show(1)