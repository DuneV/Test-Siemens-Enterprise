from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    # Logos
    # dbc.Row(
    #     [
    #         dbc.Col(html.Img(src="/assets/logo-siemens.png", height="100px"), width=6, className="d-flex justify-content-center")
    #     ],
    #     justify="center",
    #     align="center",
    #     style={"margin": "50px auto"},
    # ),
    # html.Hr(),
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
                    dcc.Dropdown(  # Cambiado a Dropdown
                        id='input-1',  # Mismo ID para que siga funcionando
                        options=[
                            {'label': 'P1', 'value': 'P1'},
                            {'label': 'P2', 'value': 'P2'},
                            {'label': 'P3', 'value': 'P3'},
                            {'label': 'P4', 'value': 'P4'},
                            {'label': 'P5', 'value': 'P5'},
                            {'label': 'P6', 'value': 'P5'},
                            {'label': 'P7', 'value': 'P7'},
                            {'label': 'P8', 'value': 'P8'},
                            {'label': 'P9', 'value': 'P9'},
                            {'label': 'P10', 'value': 'P10'}, 
                            {'label': 'P11', 'value': 'P11'},
                            {'label': 'P12', 'value': 'P12'},
                        ],
                        placeholder='Selecciona el Periodo',
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
                        placeholder='First year Fail',
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