from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, extratos, dashboards

from globals import *




# =========  Layout  =========== #
content = html.Div(id="page-content")


# boas praticas para montagem de linhas e colunas usando o dbc.Container
app.layout = dbc.Container(children=[
    # criando copias pra armazenar em cache do navegador sem utilizar variaveis globais
    dcc.Store(id='store-receitas', data=df_receitas.to_dict()),
    dcc.Store(id='store-despesas', data=df_despesas.to_dict()),
    dcc.Store(id='store-cat-receitas', data=df_cat_receita.to_dict()),
    dcc.Store(id='store-cat-despesas', data=df_cat_despesa.to_dict()),
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
            # #edf2fa = cinza claro
        ], md=2, style={'background-color': '#edf2fa', 'height':'1080px'}),
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
    
    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)