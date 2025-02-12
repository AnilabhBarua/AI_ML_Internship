# BAR CHART

#A bar graph looks similar to a histogram consisting of a set of bars based on the data but there are some major
#differences between a bar chart and a histogram.
#While the histogram displays the frequency of numerical
#data, a bar chart uses bars to compare different categories of data.
#One noticeable difference is that there are gaps between bars in a bar chart but in a histogram, the bars are placed
#adjacent to each other.
#Thus, if it quantitative data, histograms should be used, whereas if it is qualitative data, the bar chart can be used.

#Program 2: Designing a Bar Chart
import matplotlib.pyplot as plt
import numpy as np
#Creating an array of categorical data
data = ('Fortran', 'C', 'C++', 'Java', 'R', 'Python')
p = [1,2,4,6,8,10]
y = np.arange(len(data))
#Plotting the Bar Graph
plt.bar(y, p, align='center', alpha=0.5, edgecolor='black')
plt.xlabel('Programming Languages')
plt.ylabel('No. of Usage')
plt.title('Programming Languages Used in Projects')
plt.show()
