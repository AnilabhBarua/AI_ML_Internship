# Example Python program to draw a percentage
# based area plot(stacked) for a Python pandas DataFrame
import pandas as pd
import matplotlib.pyplot as plot
zonalRevenue = {"East"   : (25, 27, 32, 31),
                "West"  :  (32, 40, 39, 44),
                "South"  : (34, 31, 32, 34),
                "North"  : (27, 26, 22, 28)
                };
dataFrame           = pd.DataFrame(data=zonalRevenue);
# Normalize Data
normalizedDataFrame = dataFrame.div(dataFrame.sum(axis=1), axis=0);
years     = ("2016", "2017", "2018", "2019");
normalizedDataFrame.index = years;
# Draw a percentage based, stacked area plot
normalizedDataFrame.plot.area(stacked=True);
plot.show(block=True);
