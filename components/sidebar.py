import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
                # Titulo
                html.H2('MyBudget', className='text-primary'),
                # Paragrafo
                html.P('By Diego Policarpo', className='text-info'),
                # Quebra de linha
                html.Hr(),
                
    # Seção PERFIL -----------------------------
                dbc.Button(id='botao-avatar',
                           children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                            ], style={'backgroud-color': 'transparent', 'border-color': 'transparent'}),
                
    # Seção NOVO -------------------------------
                dbc.Row([
                    dbc.Col([
                        dbc.Button(color='success', id='open-novo-receita',
                                   children=['+ Receita'])
                    ], width=6),
                    dbc.Col([
                        dbc.Button(color='danger', id='open-novo-despesa',
                                   children=['- Despesa'])
                    ], width=6)
                ]),
                
                # Modal Receita
                dbc.Modal([ 
                    dbc.ModalHeader(dbc.ModalTitle('Adiciona receita')),
                    dbc.ModalBody([
                        
                    ])
                ], id='modal-novo-receita'),
                
                # Modal Despesa
                dbc.Modal([ 
                    dbc.ModalHeader(dbc.ModalTitle('Adiciona despesa')),
                    dbc.ModalBody([
                        
                    ])
                ], id='modal-novo-despesa'),
                
    # Sesão NAV ------------------------------
                html.Hr(),
                dbc.Nav([
                    dbc.NavLink('Dashboard', href='/dashboards', active='exact'),
                    dbc.NavLink('Extratos', href='/extratos', active='exact'),                    
                ], vertical=True, pills=True, id='nav_buttons', style={'margin-bottom': '50px'}),  
                
                
                
                
                
                
                
], id='sidebar_completa')





# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-uip despesa    
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open