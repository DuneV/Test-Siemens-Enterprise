from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
                    dbc.Row(
                    html.H2(
                        "KPI's Module - DT", 
                        style={
                            'color': 'white'
                        }
                    ), 
                    style={
                        'text-align': 'center',
                        'background-image': 'linear-gradient(to right, #1B1534, #4D217A 50%, #1B1534)',  
                        'padding': '20px'
                    }),
    dbc.Row([
        dbc.Button('General Report', id='general-report'),
        
        dbc.Col(
        dbc.Button('OTD', id='btn-2')),
        
        dbc.Col(
        dbc.Button('FPY', id='btn-3')),
        
        dbc.Col(
        dbc.Button('3i', id='btn-4')),
        
        dbc.Col(
        dbc.Button('NCC', id='btn-5')),
            ]),
    dbc.Row([
        dbc.Col( 
        dbc.Button('Provisions', id='btn-6')),
        dbc.Col(
        dbc.Button('TRIR', id='btn-7')),
        dbc.Col(
        dbc.Button('Productivity', id='btn-8')),
        dbc.Col(
        dbc.Button('PVO', id='btn-9')),
        dbc.Col(
        dbc.Button('Labs', id='btn-10')),
        html.Div(id='container')
        ])
], fluid=True)


# layout = dbc.Container([
    # dbc.Row(
    #     html.H2(
    #         "KPI's Module - DT", 
    #         style={
    #             'color': 'white'
    #         }
    #     ), 
    #     style={
    #         'text-align': 'center',
    #         'background-image': 'linear-gradient(to right, #1B1534, #4D217A 50%, #1B1534)',  
    #         'padding': '20px'
    #     }
    # ),
#     # Fila con un solo botón en el centro
#     dbc.Row(
#         dbc.Col(
#             html.Button(
#                 "General Report",
#                 id="card-button",
#                 n_clicks=0,
#                 className="card-button"
#             ),
#             width=12,  # Centramos el botón
#             style={'text-align': 'center', 'margin-top': '20px'}
#         )
#     ),
#     dbc.Row([
#         dbc.Col(
#             html.Button("OTD", id="otd-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             html.Button("FPY", id="fpy-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             dbc.Button("3i", id="3i-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             dbc.Button("NCC", id="ncc-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#     ],
#     style={'text-align': 'center', 'margin-top': '20px'}
#     ),

#     dbc.Row([
#         dbc.Col(
#             dbc.Button("Provisions", id="provisions-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             dbc.Button("TRIR", id="trir-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             dbc.Button("Productivity", id="productivity-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             dbc.Button("PVO", id="pvo-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#         dbc.Col(
#             dbc.Button("Lab Invoices", id="lab-button", n_clicks=0, className="card-button"),
#             width=2
#         ),
#     ],
#     style={'text-align': 'center', 'margin-top': '20px'}
#     )
# ], fluid=True)