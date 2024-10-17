# src/home/callbacks.py
import sqlite3
from dash import Input, Output, State, callback
import dash_bootstrap_components as dbc

from app import app  # Importar la instancia de la aplicación

# Callback para procesar los datos ingresados manualmente

@callback(
    Output('output-data', 'children'),
    Input('submit-button', 'n_clicks'),
    [State('input-1', 'value'), 
     State('input-2', 'value'),
     State('input-3', 'value'),
     State('input-4', 'value')]
)
def process_manual_input(n_clicks, input1, input2, input3, input4):
    if n_clicks > 0:
        try:
            # Validaciones adicionales
            if input1 is None or input2 is None or input3 is None or input4 is None:
                return dbc.Alert("Por favor, ingresa todos los valores.", color="danger")
            
            # conn = sqlite3.connect('my_database.db')  # Reemplazar con la conexión a tu base de datos
            # cursor = conn.cursor()
            
            # # Crear una tabla si no existe
            # cursor.execute('''CREATE TABLE IF NOT EXISTS inputs (
            #                     id INTEGER PRIMARY KEY AUTOINCREMENT,
            #                     input1 TEXT,
            #                     input2 TEXT,
            #                     input3 TEXT
            #                   )''')
            
            # # Insertar los valores en la tabla
            # cursor.execute("INSERT INTO inputs (input1, input2, input3) VALUES (?, ?, ?)", 
            #                (input1, input2, input3))
            
            # # Guardar los cambios
            # conn.commit()

            # # Cerrar la conexión
            # conn.close()


            # Procesar los valores ingresados
            # Aquí puedes agregar cualquier lógica adicional de procesamiento si es necesario
            result = f'Valores ingresados: {input1}, {input2}, {input3}, {input4}'      

            # Mensaje de éxito
            success_msg = dbc.Alert(result, color="success")
            return success_msg
        except Exception as e:
            # Mensaje de error
            error_msg = dbc.Alert(f"Hubo un error al procesar los datos: {str(e)}", color="danger")
            return error_msg
    return ''
