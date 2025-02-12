import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("tips.csv")

plt.bar(data['day'],data['tip'])

plt.title("bar chart")

plt.xlabel('day')
plt.ylabel("tip")
plt.show 