# src/interferences/layout.py

from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("Detección y Filtrado de Interferencias", style={'margin-top': '20px'}),
    html.Hr(),
    # Contenedor para el contenido dinámico
    html.Div(id='interference-content'),
])
