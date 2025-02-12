import pandas as pd
data={
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    }
# load data into a DataFrame Object:
df=pd.DataFrame(data)
print(df)
