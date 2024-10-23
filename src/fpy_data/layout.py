# src/fpy_data/layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

# Layout for FPY Data page
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("FPY Data", className="text-center")),
                dbc.Col(
                    # dbc.Button("New FPY", color="primary", className="ml-auto"), width="auto"
                    html.Button('New FPY', id='fpy-button', n_clicks=0, className='btn btn-primary'),
                    width={"size": 4, "offset": 4},
                    # className="d-flex justify-content-rigth",
                    # style={"marginTop": "20px"}
                ),
            ],
            justify="between",  # Align items horizontally
        ),
        html.Br(),
        
        # Filters section
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                    id='fiscal-year-dropdown',
                    options=[
                        {'label': '2024', 'value': '2024'},
                        {'label': '2023', 'value': '2023'}
                    ],
                    placeholder="Select FY",
                    className="mb-3"
                )),
                dbc.Col(dcc.Dropdown(
                    id='month-dropdown',
                    options=[
                        {'label': 'P01', 'value': 'P01'},
                        {'label': 'P02', 'value': 'P02'}
                    ],
                    placeholder="Select Month",
                    className="mb-3"
                )),
                dbc.Col(dcc.Dropdown(
                    id='production-line-dropdown',
                    options=[
                        {'label': 'SDT', 'value': 'SDT'},
                        {'label': 'MDT', 'value': 'MDT'}
                    ],
                    placeholder="Select Production Line",
                    className="mb-3"
                )),
                dbc.Col(dbc.Input(
                    id='tested-units-input',
                    type='number',
                    placeholder="Tested Units",
                    className="mb-3"
                )),
                dbc.Col(dbc.Input(
                    id='failed-units-input',
                    type='number',
                    placeholder="Failed Units",
                    className="mb-3"
                )),
            ],
            className="mb-4"
        ),
        
        # Data Tables section
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("SDT", className="card-title"),
                                html.P("FY: 2024 | Month: P01"),
                                html.P("Tested Units: 100 | Failed Units: 1"),
                            ]
                        ),
                    ), width=4
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("MDT", className="card-title"),
                                html.P("FY: 2024 | Month: P03"),
                                html.P("Tested Units: 1000 | Failed Units: 1"),
                            ]
                        ),
                    ), width=4
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("LDT", className="card-title"),
                                html.P("No data available"),
                            ]
                        ),
                    ), width=4
                ),
            ],
        ),
    ],
    fluid=True,
    className="p-4",
)
