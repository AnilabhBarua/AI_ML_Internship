# importing the modules
from bokeh.plotting import figure, output_file, show
import pandas as pd
# instantiating the figure object
graph = figure(title = "Bokeh Bar Chart")
# reading the database
data = pd.read_csv("tips.csv")
# plotting the graph
graph.vbar(data['total_bill'], top=data['tip'], legend_label = "Bill VS Tips", color='green')
graph.vbar(data['tip'], top=data['size'], legend_label = "Tips VS Size", color='red')
graph.legend.click_policy = "hide"
# displaying the model
show(graph)
