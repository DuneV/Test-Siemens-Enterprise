# src/interferences/callbacks.py

from dash import Input, Output, State, callback, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from app import app  # Importar la instancia de la aplicación
from .logic import (
    detect_interferences,
    generate_interference_table,
    generate_interference_spectrum,
    generate_suavizado_plot
)

@callback(
    Output('interference-content', 'children'),
    Input('stored-data', 'data'),
)
def update_interference_analysis(data_json):
    """
    Callback para actualizar el contenido de la página de interferencias.

    Parameters:
    - data_json: str (JSON)
        Datos almacenados en 'stored-data', en formato JSON.

    Returns:
    - content: list of Dash components
        Contenido a mostrar en la página, ya sea la alerta o los componentes de interferencia.
    """
    if data_json is None:
        # Si no hay datos, mostrar una alerta
        alert_message = dbc.Alert(
            "No hay datos cargados. Por favor, sube un archivo CSV en la sección Inicio.",
            color="warning",
            dismissable=False,
            style={'text-align': 'center'}
        )
        return alert_message
    else:
        # Convertir los datos de JSON a DataFrame
        df = pd.read_json(data_json, orient='split')

        # Detectar interferencias
        interference_list = detect_interferences(df)

        # Guardar la lista de interferencias en un componente de almacenamiento oculto
        interference_data = pd.DataFrame(interference_list).to_json(date_format='iso', orient='split')

        # Generar tabla de interferencias
        interference_table = generate_interference_table(interference_list)

        # Generar espectro con interferencias marcadas
        interference_spectrum_fig = generate_interference_spectrum(df, interference_list)

        # Generar gráfico de efecto del suavizado
        suavizado_fig = generate_suavizado_plot(df)

        # Construir el contenido completo
        content = [
            # Componente oculto para almacenar la lista de interferencias
            dcc.Store(id='stored-interferences', data=interference_data),
            # Sección para mostrar la tabla de interferencias detectadas
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Interferencias Detectadas"),
                            interference_table,
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
            # Gráfico del Espectro con Interferencias
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Espectro con Interferencias Marcadas"),
                            dcc.Graph(figure=interference_spectrum_fig),
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
            # Gráfico de Efecto del Suavizado
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Efecto del Suavizado"),
                            dcc.Graph(figure=suavizado_fig)
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
        ]

        return content

