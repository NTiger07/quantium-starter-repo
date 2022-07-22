from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from pandas import DataFrame, read_csv
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

data = read_csv('./complete.csv')
date = data['date']
sales = data['sales($)']
north = data[data['region']=='north']['sales($)']
south = data[data['region']=='south']['sales($)']
east = data[data['region']=='east']['sales($)']
west = data[data['region']=='west']['sales($)']
north_date = data[data['region']=='north']['date']
south_date = data[data['region']=='south']['date']
east_date = data[data['region']=='east']['date']
west_date = data[data['region']=='west']['date']


app.layout = html.Div([
    html.H4('Total sales($) of pink morsel by Soul Foods'),
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
    df = DataFrame(data)
    if value == 'North':
        fig = px.line(north, 
        x = north_date, y=north).update_layout(xaxis_title="Date", yaxis_title="Sales($) at North")
        fig.update_traces(line_color = '#430802')
        return fig
    elif value == 'South':
        fig = px.line(south, 
        x = south_date, y=south).update_layout(xaxis_title="Date", yaxis_title="Sales($) at South")
        fig.update_traces(line_color = '#C0D1EB')
        return fig
    elif value == 'East':
        fig = px.line(east, 
        x = east_date, y=east).update_layout(xaxis_title="Date", yaxis_title="Sales($) at East")
        fig.update_traces(line_color = '#5F3509')
        return fig
    elif value == 'West':
        fig = px.line(west, 
        x = west_date, y=west).update_layout(xaxis_title="Date", yaxis_title="Sales($) at West")
        fig.update_traces(line_color = 'black')
        return fig
    else:
        fig = px.line(df[data['region'].str.contains('south')], 
            x = date, y=sales).update_layout(xaxis_title="Date", yaxis_title="Total Sales($)")
        return fig


app.run_server(debug=True)