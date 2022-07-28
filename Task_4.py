from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from pandas import read_csv

app = Dash(__name__)

data = read_csv('./complete.csv')
total_date = data['date']
total_sales = data['sales($)']

#sales values
north_sales = data[data['region']=='north']['sales($)']
south_sales = data[data['region']=='south']['sales($)']
east_sales = data[data['region']=='east']['sales($)']
west_sales = data[data['region']=='west']['sales($)']

#date values
north_date = data[data['region']=='north']['date']
south_date = data[data['region']=='south']['date']
east_date = data[data['region']=='east']['date']
west_date = data[data['region']=='west']['date']


app.layout = html.Div([
    html.H4(id="title", children="Total sales($) of pink morsel by Soul Foods"),
    dcc.Graph(id="graph"),
    dcc.RadioItems(
        id="radio",
        options=["All", "North", "South","East","West"],
        value="All",
        inline=True
    ),
])

@app.callback(
    Output("graph", "figure"), 
    Input("radio", "value"))

def update_line_chart(value):
    if value == 'North':
        fig = px.line(x = north_date, y=north_sales).update_layout(xaxis_title="Date", yaxis_title="Sales($) at North")
        fig.update_traces(line_color = '#430802')
        return fig
    elif value == 'South':
        fig = px.line(x = south_date, y=south_sales).update_layout(xaxis_title="Date", yaxis_title="Sales($) at South")
        fig.update_traces(line_color = '#C0D1EB')
        return fig
    elif value == 'East':
        fig = px.line( x = east_date, y=east_sales).update_layout(xaxis_title="Date", yaxis_title="Sales($) at East")
        fig.update_traces(line_color = '#5F3509')
        return fig
    elif value == 'West':
        fig = px.line(x = west_date, y=west_sales).update_layout(xaxis_title="Date", yaxis_title="Sales($) at West")
        fig.update_traces(line_color = 'black')
        return fig
    else:
        fig = px.line(x = total_date, y=total_sales).update_layout(xaxis_title="Date", yaxis_title="Total Sales($)")
        return fig


app.run_server(debug=True)