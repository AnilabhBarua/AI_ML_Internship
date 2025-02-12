from bokeh.plotting import figure
from bokeh.io import save, output_file, show
output_file("AA.html")
x=[1, 2, 3, 4, 5]
y=[5, 7, 2, 4, 5]
graph=figure(title="simple example", x_axis_label="x", y_axis_label="y")
graph.line(x,y, legend_label="temp.", line_width=2)
save(graph,"BB.html", title="Test")
show(graph)
