import sqlite3
from dash import Input, Output, State, callback
import dash_bootstrap_components as dbc

from app import app  # Importar la instancia de la aplicación

# Callback para procesar los datos ingresados manualmente
@callback(
    Output('output-data', 'children'),
    Input('submit-button', 'n_clicks'),
    [State('input-1', 'value'),  # Dropdown
     State('input-2', 'value'),  # Input numérico
     State('input-3', 'value'),  # Input numérico
     State('input-4', 'value')]  # Input numérico
)
def process_manual_input(n_clicks, input1, input2, input3, input4):
    if n_clicks > 0:
        try:
            # Validaciones adicionales
            if input1 is None or input2 is None or input3 is None or input4 is None:
                return dbc.Alert("Por favor, ingresa todos los valores.", color="danger")

            # Procesar los valores ingresados
            result = f'Valores ingresados: Periodo: {input1}, FY: {input2}, Units tested: {input3}, Units Failed: {input4}'      

            # Mensaje de éxito
            success_msg = dbc.Alert(result, color="success")
            return success_msg
        except Exception as e:
            # Mensaje de error
            error_msg = dbc.Alert(f"Hubo un error al procesar los datos: {str(e)}", color="danger")
            return error_msg
    return ''
