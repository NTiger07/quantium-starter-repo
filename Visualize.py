from pandas import read_csv
import plotly.express as px

#read data from file
data = read_csv('./complete.csv')
date = data['date']
sales = data['sales($)']

#display data on line_graph.html
fig = px.line(x = date, y = sales, title = 'Total sales($) of pink morsel by Soul Foods').update_layout(xaxis_title="Date", yaxis_title="Sales($)")
fig.write_html('line_graph.html', auto_open=True)
