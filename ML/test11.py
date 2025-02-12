# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# reading the database
data = pd.read_csv("tips.csv")
# using only data attribute
sns.lineplot(data=data.drop(['total_bill'], axis=1))
plt.show()
