#Pie Chart

#A pie chart, as the name suggests, looks similar to a pie. ▪ Pie charts are best to use when one is trying to compare parts of a whole.
#It is a circular graphic that is divided into slices. ▪ Each slice indicates a statistical numerical proportion based on the data provided.
#The arc length of each slice of a pie is proportional to the quantity it represents.
#A pie chart has several variations and can be presented in several ways.

#Program 3: Displaying Pie Chart
import matplotlib.pyplot as plt
# Data to plot
l = ['Data Science', 'Soft Computing', 'Cloud Computing', 'Mean Stack']
sizes = [40, 20, 15, 25] # percentages
# Create pie chart
plt.pie(sizes, labels=l, autopct='%1.1f%%')
# Add title
plt.title('MCA Elective Distribution')
# Show plot
plt.show()
