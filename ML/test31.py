#HEAT MAP
#A heat map represents data in a two-dimensional format in which each data value is represented by a color in the matrix.
#Since colors play a major role in displaying a heat map, many different color schemes can be used for illustrating a heat map.
#Heat maps are often used to display correlation matrix.
#Heat maps rely on colors to express the variation in data – the darker shades of color indicate more quantity or more
#correlation while the lighter shades of color indicate less quantity or less correlation.
#This graphic representation thus provides an immediate meaningful visual summary of information.

#Program 5: Displaying Heat Map
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Load data into a pandas DataFrame
data = pd.DataFrame({
'A': [1, 2, 3, 4, 5],
'B': [5, 4, 3, 2, 1],
'C': [2, 4, 6, 8, 10],
'D': [10, 8, 6, 4, 2],
'E': [3, 5, 7, 9, 11]
})
# Create heatmap
sns.heatmap(data, annot=True)
# Add title
plt.title('Sample Data Heatmap')
# Show plot
plt.show()
