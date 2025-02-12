# Python Code for Data Transformation
import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s
#Creating Data Frame
d={'C1':[1,3,7,4],'C2':[12,2,7,1],'C3':[22,34,-11,9]}
df2=pd.DataFrame(d)
print("\n Original Data Values")
print("---------")
print(df2)
# rescaling method1: MinMax
print("\n\n Data Scaled Between 0 and 1")
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled=data_scaler.fit_transform(df2)
print("\n Min Max Scaled data")
print("------------")
print(data_scaled.round(3))
#rescaling method2: Normalizing
dn=preprocessing.normalize(df2, norm='l1')
print("\n L1 Normalized data")
print("------------------")
print(dn.round(2))
