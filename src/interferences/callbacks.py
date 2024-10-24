# src/interferences/callbacks.py

from dash import Input, Output, State, callback, html, dcc, ctx
import dash_bootstrap_components as dbc
import json
import pandas as pd

from app import app  

# Callbacks para manejar los botones

@callback(Output('container', 'children'),
              Input('general-report', 'n_clicks'),
              Input('btn-2', 'n_clicks'),
              Input('btn-3', 'n_clicks'),
              Input('btn-4', 'n_clicks'),
              Input('btn-5', 'n_clicks'),
              Input('btn-6', 'n_clicks'),
              Input('btn-7', 'n_clicks'),
              Input('btn-8', 'n_clicks'),
              Input('btn-9', 'n_clicks'),
              Input('btn-10', 'n_clicks'))


def display(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10):
    button_id = ctx.triggered_id if not None else 'No clicks yet'

    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Table([
            html.Tr([html.Th('Button 1'),
                     html.Th('Button 2'),
                     html.Th('Button 3'),
                     html.Th('Button 4'),
                     html.Th('Button 5'),
                     html.Th('Button 6'),
                     html.Th('Button 7'),
                     html.Th('Button 8'),
                     html.Th('Button 9'),
                     html.Th('Button 10'),
                     html.Th('Most Recent Click')]),
            html.Tr([html.Td(btn1 or 0),
                     html.Td(btn2 or 0),
                     html.Td(btn3 or 0),
                     html.Td(btn4 or 0),
                     html.Td(btn5 or 0),
                     html.Td(btn6 or 0),
                     html.Td(btn7 or 0),
                     html.Td(btn8 or 0),
                     html.Td(btn9 or 0),
                     html.Td(btn10 or 0),
                     html.Td(button_id)])
        ]),
        html.Pre(ctx_msg)
    ])


# @callback(
#     Output('interference-content', 'children'),  # Actualiza el contenido según el botón
#         Input('card-button', 'n_clicks'),
#         Input('otd-button', 'n_clicks'),
#         Input('fpy-button', 'n_clicks'))


# def handle_card_click(btn1, btn2, btn3):
#     button_id = ctx.triggered_id if not None else 'No clicks yet'
#     ctx_msg = json.dumps({
#             'states': ctx.states,
#             'triggered': ctx.triggered,
#             'inputs': ctx.inputs
#         }, indent=2)
#     print(ctx_msg)
#     return "Click en una tarjeta para ver detalles."