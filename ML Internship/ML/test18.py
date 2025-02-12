# importing the modules
from bokeh.plotting import figure, output_file, show
import pandas as pd
# instantiating the figure object
graph = figure(title = "Bokeh Bar Chart")
# reading the database
data = pd.read_csv("tips.csv")
# plotting the graph
graph.vbar(data['total_bill'], top=data['tip'])
# displaying the model
show(graph)
