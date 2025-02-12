
#Donut charts are the modified version of Pie Charts with the area of center cut out.
#A donut is more concerned about the use of area of arcs to represent the information
#in the most effective manner instead of Pie chart which is more focused on comparing
#the proportion area between the slices. Donut charts are more efficient in terms of space
#because the blank space inside the donut charts can be used to display some additional
#information about the donut chart.

#For being a Donut chart it must be necessarily a Pie chart.
#If we look at the pie chart, we will focus on the center of the chart.
#Donut charts, on the other hand, eliminates the need to compare the size
#or area of the slice and shifts the focus on the length of the arc, which
#in turn is easy to measure.

#Creating a Donut Chart involves three simple steps which are as follows :
# 1. Create a Pie Chart
# 2. Draw a circle of suitable dimensions.
# 3. Add circle at the Center of Pie chart

import matplotlib.pyplot as plt
# Setting labels for items in Chart
Employee = ['Roshni', 'Shyam', 'Priyanshi',
            'Harshit', 'Anmol']
# Setting size in Chart based on
# given values
Salary = [40000, 50000, 70000, 54000, 44000]
# colors
colors = ['#FF0000', '#0000FF', '#FFFF00',
          '#ADFF2F', '#FFA500']
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05)
# Pie Chart
plt.pie(Salary, colors=colors, labels=Employee,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)
# Adding Title of chart
plt.title('Employee Salary Details')
# Add Legends
plt.legend(loc="upper right", title="Salary Color")
# Displaying Chart
plt.show()
