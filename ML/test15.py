# importing the modules
from bokeh.plotting import figure, output_file, show
import pandas as pd
import matplotlib.pyplot as plt
# instantiating the figure object
graph = figure(title = "Bokeh Bar Chart")
# reading the database
data = pd.read_csv("tips.csv")
# Count of each unique value of
# tip column
df = data['tip'].value_counts()
# plotting the graph
graph.line(df, data['tip'])
# displaying the model
show(graph)
