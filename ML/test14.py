# importing the modules
from bokeh.plotting import figure
from bokeh.io import save, output_file, show
from bokeh.palettes import magma
import pandas as pd
# instantiating the figure object
graph = figure(title = "Bokeh Scatter Graph")
# reading the database
data = pd.read_csv("tips.csv")
color = magma(244)
# plotting the graph
graph.scatter(data['total_bill'], data['tip'], color=color)
# displaying the model
show(graph)
