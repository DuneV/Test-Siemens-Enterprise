# src/signal_analysis/layout.py

from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.H2("Análisis de Señal", style={'margin-top': '20px'}),
    html.Hr(),
    # Contenedor para el contenido dinámico
    html.Div(id='signal-analysis-content'),
])
