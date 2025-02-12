# Example Python program to draw an overlapped area plot
# for a pandas DataFrame
import pandas as pd
import matplotlib.pyplot as plot
# Peak Temperature data for two cities
tempData    = {"City1":[99, 106, 102, 78],
              "City2":[77, 84, 80, 85]};
# Seasons              
seasons     = ("Spring", "Summer", "Fall", "Winter");
# Create a DataFrame instance
dataFrame   = pd.DataFrame(tempData, index=seasons);
#Draw an area plot for the DataFrame data
dataFrame.plot(kind='area', stacked=False)
plot.show(block=True);
