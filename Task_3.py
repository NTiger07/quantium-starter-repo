from pandas import read_csv
import plotly.express as px

#read data from file
data = read_csv('./complete.csv')
date = data['date']
sales = data['sales($)']
region = data['region']

#optional sorting
north = data[data['region'].str.contains('north')]
south = data[data['region'].str.contains('south')]
east = data[data['region'].str.contains('east')]
west = data[data['region'].str.contains('west')]

#display data on line_graph.html
fig = px.line(x = date, y = sales, title = 'Total sales($) of pink morsel by Soul Foods').update_layout(xaxis_title="Date", yaxis_title="Sales($)")
fig.write_html('line_graph.html', auto_open=True)
