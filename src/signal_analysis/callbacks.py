# src/signal_analysis/callbacks.py

from dash import Input, Output, State, callback, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from app import app  # Importar la instancia de la aplicación
from .logic import (
    calculate_signal_parameters,
    generate_signal_spectrum,
    generate_signal_spectrogram,
    generate_inverse_fourier_figure  # Importar la nueva función
)

@callback(
    Output('signal-analysis-content', 'children'),
    Input('stored-data', 'data')
)
def update_signal_analysis(data_json):
    """
    Callback para actualizar el contenido de la página de análisis de señal.

    Parameters:
    - data_json: str (JSON)
        Datos almacenados en 'stored-data', en formato JSON.

    Returns:
    - content: list of Dash components
        Contenido a mostrar en la página, ya sea la alerta o los parámetros y gráficos.
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

        # Calcular los parámetros de la señal
        signal_params_dict = calculate_signal_parameters(df)
        signal_params = []
        for param_name, param_value in signal_params_dict.items():
            if isinstance(param_value, np.ndarray):
                # Si el valor es un arreglo (por ejemplo, frecuencias espurias), mostrar como lista
                param_value_formatted = ', '.join([f"{val:.2f}" for val in param_value])
            else:
                param_value_formatted = f"{param_value}"
            signal_params.append(
                html.Div([
                    html.H5(param_name),
                    html.P(param_value_formatted),
                ])
            )

        # Generar el espectro de la señal
        spectrum_fig = generate_signal_spectrum(df)

        # Generar el espectrograma de la señal (Análisis de Espectro Temporal)
        spectrogram_fig = generate_signal_spectrogram(df)

        # Generar la figura de la Transformada Inversa de Fourier
        inverse_fourier_fig = generate_inverse_fourier_figure(df)

        # Construir el contenido completo
        content = [
            # Sección para mostrar los parámetros calculados
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Parámetros de la Señal", style={'margin-bottom': '25px'}),
                            html.Div(signal_params, style={
                                'display': 'grid',
                                'grid-template-columns': '1fr 1fr 1fr',
                                'gap': '10px',
                            }),
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
            # Gráfico del Espectro de la Señal
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Espectro de la Señal"),
                            dcc.Graph(figure=spectrum_fig),
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
            # Gráfico del Espectrograma (Análisis de Espectro Temporal)
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Análisis de Espectro Temporal (Waterfall Display)"),
                            dcc.Graph(figure=spectrogram_fig),
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
            # Gráfico de la Transformada Inversa de Fourier
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Transformada Inversa de Fourier"),
                            dcc.Graph(figure=inverse_fourier_fig),
                        ],
                        width=12,
                    ),
                ],
                className='mb-4',
            ),
        ]

        return content
