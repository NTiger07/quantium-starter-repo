from pandas import read_csv
import plotly.express as px
from dash import Dash, html, dcc

#instantiate app
app = Dash(__name__)

#read data from file
data = read_csv('./complete.csv')
date = data['date']
sales = data['sales($)']
region = data['region']

#line graph
fig = px.line(x = date, y = sales, title = 'Total sales($) of pink morsel by Soul Foods').update_layout(xaxis_title="Date", yaxis_title="Sales($)")

#app layout
app.layout = html.Div([
    dcc.Graph(id="graph", figure = fig)
])

app.run_server(debug=True)
