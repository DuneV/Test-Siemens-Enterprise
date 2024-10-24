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
                    html.Br(),
    dbc.Row([
        dbc.Button([html.Div([html.Img(src='/assets/icons/plug.png', style={'height': '40px', 'width': '40px'}), ], style={'textAlign': 'center'}),(),
        html.Span('General Report', style={'textAlign': 'center'})
        ], id='general-report', outline=True, color="secondary", className="mx-auto", style={'width': '96%'}),
    ], ),
    html.Br(),
    dbc.Row([
        dbc.Button([html.Div([html.Img(src='/assets/icons/plug.png', style={'height': '40px', 'width': '40px'}), ], style={'textAlign': 'center'}),(),
        html.Span('OTD', style={'textAlign': 'center'})
        ], id='btn-2', outline=True, color="secondary", className="mx-auto", style={'width': '24%'}),
        
        dbc.Button([html.Div([html.Img(src='/assets/icons/plug.png', style={'height': '40px', 'width': '40px'}), ], style={'textAlign': 'center'}),(),
        html.Span('FPY', style={'textAlign': 'center'})
        ], id='btn-3', outline=True, color="secondary", className="mx-auto", style={'width': '24%'}),
    
        dbc.Button([html.Div([html.Img(src='/assets/icons/plug.png', style={'height': '40px', 'width': '40px'}), ], style={'textAlign': 'center'}),(),
        html.Span('3i', style={'textAlign': 'center'})
        ], id='btn-4', outline=True, color="secondary", className="mx-auto", style={'width': '24%'}),
        
        dbc.Button([html.Div([html.Img(src='/assets/icons/plug.png', style={'height': '40px', 'width': '40px'}), ], style={'textAlign': 'center'}),(),
        html.Span('NCC', style={'textAlign': 'center'})
        ], id='btn-5', outline=True, color="secondary", className="mx-auto", style={'width': '24%'}),
            ]),
    html.Br(),
    dbc.Row([
        dbc.Button('Provisions', id='btn-6'),
        dbc.Col(
        dbc.Button('TRIR', id='btn-7')),
        dbc.Col(
        dbc.Button('Productivity', id='btn-8')),
        dbc.Col(
        dbc.Button('PVO', id='btn-9')),
        dbc.Col(
        dbc.Button('Labs', id='btn-10')),
        # html.Div(id='container')
        ])
], fluid=True)