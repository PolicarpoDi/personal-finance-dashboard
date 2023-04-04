from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, extratos, dashboards




# =========  Layout  =========== #
content = html.Div(id="page-content")


# boas praticas para montagem de linhas e colunas usando o dbc.Container
app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2, style={'background-color': 'black', 'height':'1080px'}),
        dbc.Col([
            content
        ], md=10, style={'background-color': '#edf2fa', 'height':'1080px'})
    ])

# o conteudo vai ser espalhado pela tela
], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extracts':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)