#Boxplots
#Boxplots are a common statistical graphic used in case of measures of central tendency and dispersion.
#A boxplot indicates how well distributed the data in a dataset is.
#It displays the data by dividing the dataset into three quartiles and then presents the values - minimum, maximum, median, first quartile and third quartile –in the plotted graph itself.
#Boxplot can also be used to compare the distribution of data across datasets by drawing individual boxplot for each cluster of data.

#Program 4: Displaying Measures of Position in a Boxplot
#import python libraries
import pandas as pd
from scipy.stats import iqr
import matplotlib.pyplot as plt
#Create a Dataframe
d={'Name':['John','Bobby','Rihana','Madonna','Rocky','Subham','Rishab','Rahul','David','Andrew', 'Ajay','Teresa'],'Score1':[62,47,55,74,31,55,85,63,42,32,71,55]}
#print the Dataframe
df = pd.DataFrame(d) 
print(df)
#Percentile Rank of the Score1 Column in DataFrame
df['Percentile_rank']=df.Score1.rank(pct=True)
print("\n Values of Percentile Rank in the Distribution")
print(df['Percentile_rank'])
#Interquartile Range of the Score1 Column in DataFrame
i = iqr(df["Score1"])
print("Value of Interquartile Range in the Distribution = ", i)
#Boxplot Representation of the Score1 Column
print("\n Boxplot Representation of the Score1 Column")
df.boxplot(column=["Score1"],grid=True, figsize=(7,7)) 
plt.text(x=0.75, y=df["Score1"].quantile(0.75), s="3rd Quartile") 
plt.text(x=0.75, y=df["Score1"].median(), s="Median") 
plt.text(x=0.75, y=df["Score1"].quantile(0.25), s="1st Quartile") 
plt.text(x=0.75, y=df["Score1"].min(), s="Min")
plt.text(x=0.75, y=df["Score1"].max(), s="Max")
plt.text(x=0.6, y=df["Score1"].quantile(0.50), s="IQR", rotation=90, size=15)
plt.show()
