# import the libraries
import pandas as pd
import numpy as np
#Creating a DataFrame with Missing Values
df =pd.DataFrame(np.random.randn (5, 3), index=['a', 'c', 'e', 'f', 'h'],
                               columns=['C1', 'C2', 'C3'])
df = df.reindex (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("\n Reindexed Data Values")
print("-------------------------")
print(df)


#Method 1 Filling Every Missing Values with 0
#print("\n\n Every Missing Value Replaced with '0':")
#print("--------------------------------------------")
#print(df.fillna(0))

#Method 2-Dropping Rows Having Missing Values
#print("\n\n Dropping Rows with Missing Values:")
#print("----------------------------------------")
#print(df.dropna())

median = df['C1'].median()
df['C1'].fillna(median, inplace =True)
median = df['C2'].median()
df['C2'].fillna(median, inplace =True)
print("\n\n Missing Values for Column 1 Replaced with Median Value:")
print("---------------------------------------------")
print(df)
