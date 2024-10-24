# src/fpy_data/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

# Layout for FPY Data page

fpy_data_tab = dbc.Tab(
    dbc.Container(
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
                dbc.ModalHeader("Edit FPY", style={"fontWeight": "bold"}),
                dbc.ModalBody([
                    # dbc.Col(html.Td("FP", className="text-left")),
                    dbc.Label("FY"),
                
                    dbc.Input(id="modal-input-fy", placeholder="Fiscal Year", type="text"),
                    html.Br(), # cambiar por componente Hr (caso linea horizontal)
                    dbc.Label("Month"),
                    dcc.Dropdown(
                    id='modal-input-month',
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
                    ),
                    html.Br(),
                    dbc.Label("Production Line"),
                    dbc.RadioItems(
                    id="modal-input-production-line",
                    options=[
                        {"label": "SDT", "value": "SDT"},
                        {"label": "MDT", "value": "MDT"},
                        {"label": "LDT", "value": "LDT"}                    
                    ],
                    value="start",
                    inline=True,
                    ),
                    html.Br(),
                    dbc.Label("Tested Units"),
                    dbc.Input(id="modal-input-tested-units", placeholder="Tested Units", type="number"),
                    html.Br(),
                    dbc.Label("Failed Units"),
                    dbc.Input(id="modal-input-failed-units", placeholder="Failed Units", type="number"),
                ]),
                dbc.ModalFooter(
                    html.Button("Submit", id="modal-submit-button", n_clicks=0, className='btn btn-secondary float-right', style={'background-color': '#1b1534', 'color': 'white', "fontWeight": "bold"})
                ),
            ],
            id="fpy-modal",
            is_open=False
        ),
        
        # Filters section
        
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                    id='fiscal-year-dropdown',
                    options=[
                        {'label': '2024', 'value': '2024'},
                        {'label': '2023', 'value': '2023'},
                        {'label': '2022', 'value': '2022'},
                        {'label': '2021', 'value': '2021'}
                    ],
                    placeholder="Select FY",
                className="edit-inputs"), width=2), 
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
                    placeholder="Select Month", className="edit-inputs"
                ), width=2),
                dbc.Col(dcc.Dropdown(
                    id='production-line-dropdown',
                    options=[
                        {'label': 'SDT', 'value': 'SDT'},
                        {'label': 'MDT', 'value': 'MDT'},
                        {'label': 'LDT', 'value': 'LDT'}
                    ],
                    placeholder="Select Production Line", 
                    className="edit-inputs"
                ), width=2),
                dbc.Col(dbc.Input(
                    id='tested-units-input',
                    type='number',
                    placeholder="Tested Units", 
                    className="edit-inputs"
                ), width=2),
                dbc.Col(dbc.Input(
                    id='failed-units-input',
                    type='number',
                    placeholder="Failed Units", 
                    className="edit-inputs"
                ), width=2),
            ],
            className="mb-4 justify-content-center"
        ),
        
        # Tabla basada en filtros 
        
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
),
    label="FPY Data",  # Tab FPY
    tab_id= "fpy-tab",
    label_style={"color": "#4D217A"}
)

# Tab SDT
sdt_tab = dbc.Tab(
    dbc.Container(
        [
            html.Br(),
            dbc.Row(
                dbc.Col(html.H3("SDT Data Table")),
            ),
            # Content
        ],
        fluid=True,
    ),
    label= "SDT",
    tab_id= "sdt-tab",
    label_style={"color": "#4D217A"}
)

# Tab  MDT
mdt_tab = dbc.Tab(
    dbc.Container(
        [
            html.Br(),
            dbc.Row(
                dbc.Col(html.H3("MDT Data Table")),
            ),
        ],
        fluid=True,
    ),
    label= "MDT",
    tab_id= "mtd-tab",
    label_style={"color": "#4D217A"}
)

# Tab LDT
ldt_tab = dbc.Tab(
    dbc.Container(
        [
            html.Br(),
            dbc.Row(
                dbc.Col(html.H3("LDT Data Table")),
            ),
        ],
        fluid=True,
    ),
    label= "LDT",
    tab_id= "ltd-tab",
    label_style={"color": "#4D217A"}
)
layout = dbc.Container(
    [
        html.Br(),
        dbc.Tabs([fpy_data_tab, sdt_tab, mdt_tab, ldt_tab])  # Define the tabs
    ],
    fluid=True,
)
