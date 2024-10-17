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
    # Formulario para ingresar datos manualmente
    dbc.Row(
        [
            dbc.Col(
                [
                    html.Label('Period', style={'textAlign': 'center', 'display': 'block'}),
                    dcc.Input(
                        id='input-1',
                        type='number',
                        placeholder='Ingresa el valor 1',
                        style={'width': '100%', 'textAlign': 'center'}
                    )
                ],
                width=4
            ),
            dbc.Col(
                [
                    html.Label('FY', style={'textAlign': 'center', 'display': 'block'}),
                    dcc.Input(
                        id='input-2',
                        type='number',
                        placeholder='Ingresa el valor 2',
                        style={'width': '100%', 'textAlign': 'center'}
                    )
                ],
                width=4
            ),
            dbc.Col(
                [
                    html.Label('Units tested', style={'textAlign': 'center', 'display': 'block'}),
                    dcc.Input(
                        id='input-3',
                        type='number',
                        placeholder='Ingresa el valor 3',
                        style={'width': '100%', 'textAlign': 'center'}
                    )
                ],
                width=4
            ),
            dbc.Col(
                [
                    html.Label('Units Failed', style={'textAlign': 'center', 'display': 'block'}),
                    dcc.Input(
                        id='input-4',
                        type='number',
                        placeholder='Ingresa el valor 4',
                        style={'width': '100%', 'textAlign': 'center'}
                    )
                ],
                width=4
            )
            
        ],
        justify="center",
        style={"marginTop": "20px"}
    ),
    # Botón para enviar los datos
    dbc.Row(
        dbc.Col(
            html.Button('Enviar', id='submit-button', n_clicks=0, className='btn btn-primary'),
            width={"size": 4, "offset": 4},
            className="d-flex justify-content-center",
            style={"marginTop": "20px"}
        ),
    ),
    # Div para mostrar los datos ingresados
    dbc.Row(
        dbc.Col(
            html.Div(id='output-data', className='text-center'),
            width=12,
            style={"marginTop": "20px"}
        ),
    ),
    # Instrucciones
    dbc.Row(
        dbc.Col(
            html.P(
                "Por favor, ingresa los valores en los campos para comenzar el análisis.",
                className="text-center",
            ),
            width=12,
        ),
    ),
])