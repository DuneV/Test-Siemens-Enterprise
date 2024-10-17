# src/home/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    # Logos
    dbc.Row(
        [
            dbc.Col(html.Img(src="/assets/logo-siemens.png", height="100px"), width=6, className="d-flex justify-content-center")
        ],
        justify="center",
        align="center",
        style={"margin": "50px auto"},
    ),
    html.Hr(),
    # Título
    dbc.Row(
        dbc.Col(
            html.H2("Bienvenido al Análisis de Requerimientos técnicos"),
            width={"size": 8, "offset": 2},
            className="text-center",
        ),
        style={"margin-top": "50px"},
    ),
    # Botón para subir el archivo CSV
    dbc.Row(
        dbc.Col(
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Arrastra y suelta o ',
                    html.A('selecciona un archivo CSV')
                ]),
                style={
                    'width': '100%',
                    'height': '80px',
                    'lineHeight': '80px',
                    'borderWidth': '2px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=False
            ),
            width={"size": 6, "offset": 3},
        ),
    ),
    # Mensajes de error o éxito
    dbc.Row(
        dbc.Col(
            html.Div(id='upload-message', className='text-center'),
            width=12,
        ),
    ),
    # Instrucciones
    dbc.Row(
        dbc.Col(
            html.P(
                "Por favor, sube el archivo CSV para comenzar el análisis.",
                className="text-center",
            ),
            width=12,
        ),
    ),
])
