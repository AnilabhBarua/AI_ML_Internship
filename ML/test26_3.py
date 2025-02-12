# Example Python program to draw a percentage based Area
# plot for a pandas DataFrame
import pandas as pd
import matplotlib.pyplot as plot
gdpRevenue = {"Agriculture" :(200, 192, 193),
              "Dairy"       :(495, 475, 488),
              "Electronics" :(400, 418, 431),
              "Financial Services":(200, 220, 230),
              "Others"            :(150, 155, 170)
             };
index    = ("2010", "2011", "2012");
dataFrame   = pd.DataFrame(data=gdpRevenue);
normalized  = dataFrame.div(dataFrame.sum(axis=1), axis=0);
normalized.index = index;
print(normalized);
normalized.plot.area(stacked=False);
plot.show(block=True);
