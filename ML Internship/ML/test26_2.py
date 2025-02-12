# Example Python program that draws a overlapping area
# plot for a pandas DataFrame instance
import pandas as pd
import matplotlib.pyplot as plot
# Number of observations
data = [(25, 1),
        (43, 1),
        (35, 2),
        (34, 4)];
# Years
index   = ["2016", "2017", "2018", "2019"]; # (X Axis)
# Name of the Quantities corresponding to the observations(Y Axis)
columns = ["Meteors", "Meteorites"];
# Create DataFrame instance
df = pd.DataFrame(data=data, index = index, columns = columns);
# Draw an area plot that overlaps
ax = df.plot.area(stacked=True);
plot.show(block=True);
