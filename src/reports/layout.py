# src/reports/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("Generación de Reportes", style={'margin-top': '20px'}),
    html.Hr(),
    # Contenedor para el contenido dinámico
    html.Div(id='reports-content'),
])
