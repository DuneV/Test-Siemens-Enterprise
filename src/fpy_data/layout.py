# src/fpy_data/layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

# Layout for FPY Data page
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("FPY Data", className="text-left")),
                dbc.Col(
                    html.Button('New FPY', id='fpy-button', n_clicks=0, className='btn btn-secondary float-right', style={'background-color': '#1b1534', 'color': 'white', "fontWeight": "bold"} ), 
                    width="auto"
                ),
            ],
            justify="between",  # Align items 
        ),
        html.Br(),
        
        # Pop-up 
        dbc.Modal(
            [
                dbc.ModalHeader("Add New FPY Record"),
                dbc.ModalBody([
                    dbc.Input(id="modal-input-fy", placeholder="Fiscal Year", type="text"),
                    dbc.Input(id="modal-input-month", placeholder="Month", type="text"),
                    dbc.Input(id="modal-input-production-line", placeholder="Production Line", type="text"),
                    dbc.Input(id="modal-input-tested-units", placeholder="Tested Units", type="number"),
                    dbc.Input(id="modal-input-failed-units", placeholder="Failed Units", type="number"),
                ]),
                dbc.ModalFooter(
                    html.Button("Submit", id="modal-submit-button", n_clicks=0, className='btn btn-secondary float-right', style={'background-color': '#1b1534', 'color': 'white', "fontWeight": "bold"})
                ),
            ],
            id="fpy-modal",
            is_open=False,
        ),
        
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
                ), width=2),
                dbc.Col(dcc.Dropdown(
                    id='month-dropdown',
                    options=[
                        {'label': 'P01', 'value': 'P01'},
                        {'label': 'P02', 'value': 'P02'},
                        {'label': 'P03', 'value': 'P03'},
                        {'label': 'P04', 'value': 'P04'},
                        {'label': 'P05', 'value': 'P05'},
                        {'label': 'P06', 'value': 'P06'},
                        {'label': 'P07', 'value': 'P07'},
                        {'label': 'P08', 'value': 'P08'},
                        {'label': 'P09', 'value': 'P09'},
                        {'label': 'P10', 'value': 'P10'},
                        {'label': 'P11', 'value': 'P11'},
                        {'label': 'P12', 'value': 'P12'}
                    ],
                    placeholder="Select Month",
                ), width=2),
                dbc.Col(dcc.Dropdown(
                    id='production-line-dropdown',
                    options=[
                        {'label': 'SDT', 'value': 'SDT'},
                        {'label': 'MDT', 'value': 'MDT'},
                        {'label': 'LDT', 'value': 'LDT'}
                    ],
                    placeholder="Select Production Line",
                ), width=2),
                dbc.Col(dbc.Input(
                    id='tested-units-input',
                    type='number',
                    placeholder="Tested Units",
                ), width=2),
                dbc.Col(dbc.Input(
                    id='failed-units-input',
                    type='number',
                    placeholder="Failed Units",
                ), width=2),
            ],
            className="mb-4"
        ),
        
        # Table preview based on filters
        dbc.Row(
            [
                dbc.Col(
                    dbc.Table(
                        id="filtered-table",
                        bordered=True, hover=True, responsive=True, striped=True,
                    ), width=12
                ),
            ],
            className="mb-4"
        ),
        
        # Data Tables section by category (SDT, MDT, LDT)
        dbc.Row(
            [
                dbc.Col(
                    dbc.Table(
                        # SDT Table
                        children=[
                            html.Thead(html.Tr([html.Th("FY"), html.Th("Month"), html.Th("Tested Units"), html.Th("Failed Units")])),
                            html.Tbody([
                                html.Tr([html.Td("2024"), html.Td("P01"), html.Td("100"), html.Td("1")]),
                            ])
                        ],
                        bordered=True, hover=True, responsive=True, striped=True,
                    ), width=4
                ),
                dbc.Col(
                    dbc.Table(
                        # MDT Table
                        children=[
                            html.Thead(html.Tr([html.Th("FY"), html.Th("Month"), html.Th("Tested Units"), html.Th("Failed Units")])),
                            html.Tbody([
                                html.Tr([html.Td("2024"), html.Td("P03"), html.Td("1000"), html.Td("1")]),
                            ])
                        ],
                        bordered=True, hover=True, responsive=True, striped=True,
                    ), width=4
                ),
                dbc.Col(
                    dbc.Table(
                        # LDT Table
                        children=[
                            html.Thead(html.Tr([html.Th("FY"), html.Th("Month"), html.Th("Tested Units"), html.Th("Failed Units")])),
                            html.Tbody([
                                html.Tr([html.Td("No data available"), html.Td("-"), html.Td("-"), html.Td("-")]),
                            ])
                        ],
                        bordered=True, hover=True, responsive=True, striped=True,
                    ), width=4
                ),
            ],
        ),
    ],
    fluid=True,
    className="p-4",
)
