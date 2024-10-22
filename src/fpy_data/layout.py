# src/signal_analysis/layout.py

from dash import html
import dash_bootstrap_components as dbc
card = dbc.Card(
    [
        dbc.CardImg(
            src="/static/images/placeholder286x180.png",
            top=True,
            style={"opacity": 0.3},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "An example of using an image in the background of "
                        "a card.",
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="primary"),
                ],
            ),
        ),
    ],
    style={"width": "18rem"},
)
layout = dbc.Container([
    html.H2("FPY Data", style={'margin-top': '20px'}),
    html.Hr(),
    # Contenedor para el contenido dinámico
    html.Div(id='fpy-data-content'),
])


