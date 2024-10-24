# src/interferences/layout.py 

from dash import html
import dash_bootstrap_components as dbc
# import cards_kpi_super

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
    }
    ),
    dbc.Row(
        dbc.Button(
            "General Report",
            id="card-button",
            n_clicks=0
        ),
        style={'text-align': 'center', 'margin-top': '20px'}
    ),
    
    # dbc.Row(
    #     [
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-heart", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("OTD", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-cog", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("FPY", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-lightbulb", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("3I", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-trophy", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("NCC", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-percentage", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("Previsiones", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         )
    #     ],
    #     style={'margin-top': '20px'}
    # ),
    
    # dbc.Row(
    #     [
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-hands-helping", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("TRIR", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-tachometer-alt", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("Productividad", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-file-alt", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("PVO", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div([
    #                 html.I(className="fas fa-oil-can", style={'font-size': '24px', 'color': '#6c5ce7'}),
    #                 html.H5("Facturación Laboratorios", style={'margin-top': '10px'})
    #             ]),
    #             width=2
    #         ),
    #         dbc.Col(
    #             html.Div(id='interference-content'),
    #             width=2
    #         )
    #     ],
    #     style={'margin-top': '20px'}
    # )
    ], fluid=True)
