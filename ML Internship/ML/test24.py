#HISTOGRAM
#A histogram displays data distribution by creating several bars over a continuous interval.
#Each bar of a histogram signifies the tabulated frequency at each interval (or bin).
#One can estimate about data concentration via a histogram.
#Another important usage of it is displaying the extremes or outliers in datasets as well as data gaps or noisy values.

#Program 1: Designing a histogram
import matplotlib.pyplot as plt
#Creating an array of numerical data
data = [1,11,21,31,41,51]
#Plotting the histogram
plt.hist(data, bins=[0,10,20,30,40,50,60], weights=[10,1,40,33,6,8], edgecolor="red", color="green")
plt.title("An Example of a Histogram")
plt.xlabel("Data Values")
plt.show()
