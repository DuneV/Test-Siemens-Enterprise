# src/home/callbacks.py

from dash import Input, Output, State, callback
import dash_bootstrap_components as dbc
import pandas as pd

from app import app  # Importar la instancia de la aplicación
from .logic import read_csv_content  # Importar la función desde logic.py

# Callback para procesar el archivo subido
@callback(
    [Output('stored-data', 'data'),
     Output('upload-message', 'children')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def process_upload(contents, filename):
    if contents is not None and filename is not None:
        try:
            # Utilizar la función del logic.py para leer el contenido
            df = read_csv_content(contents, filename)
            # Validaciones adicionales pueden ser agregadas aquí
            # Almacenar los datos en formato JSON
            data_json = df.to_json(date_format='iso', orient='split')
            # Mensaje de éxito
            success_msg = dbc.Alert("Archivo cargado exitosamente.", color="success")
            return data_json, success_msg
        except Exception as e:
            # Mensaje de error
            error_msg = dbc.Alert(f"Hubo un error al procesar el archivo: {str(e)}", color="danger")
            return None, error_msg
    else:
        return None, ''
