# src/reports/callbacks.py

from dash import Input, Output, State, callback, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from app import app  # Importar la instancia de la aplicación
from .logic import (
    generate_report,
    get_available_content_options,
)

@callback(
    Output('reports-content', 'children'),
    Input('stored-data', 'data')
)
def update_reports_page(data_json):
    """
    Callback para actualizar el contenido de la página de reportes.

    Parameters:
    - data_json: str (JSON)
        Datos almacenados en 'stored-data', en formato JSON.

    Returns:
    - content: list of Dash components
        Contenido a mostrar en la página, ya sea la alerta o las opciones de generación de reportes.
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
        # Obtener las opciones de contenido disponibles
        content_options = get_available_content_options()

        # Crear los componentes para las opciones de contenido
        content_checklist = html.Div(
            [
                dbc.Label("Selecciona el contenido a incluir en el reporte:", html_for='report-content-options'),
                dbc.Checklist(
                    options=content_options,
                    value=[option['value'] for option in content_options],
                    id='report-content-options',
                ),
            ],
            className='mb-3',
        )

        # Campos adicionales para personalización
        additional_info = html.Div(
            [
                dbc.Label("Comentarios adicionales:", html_for='additional-comments'),
                dbc.Textarea(id='additional-comments', placeholder="Escribe aquí tus comentarios..."),
            ],
            className='mb-3',
        )

        # Botón para generar el reporte
        generate_button = dbc.Button("Generar Reporte", id='generate-report-btn', color="primary")

        # Espacio para mostrar el enlace de descarga
        download_link = dbc.Button(id='download-link', color='success', style={'display': 'none'})

        # Construir el contenido completo
        content = [
            dbc.Form(
                [
                    content_checklist,
                    additional_info,
                    dbc.Row([
                        generate_button,
                        download_link
                    ], style={'display': 'flex', 'gap': '10px', 'flex-direction': 'row'})
                ]
            )
        ]

        return content

# Callback para generar el reporte y proporcionar el enlace de descarga
@callback(
    Output('download-link', 'children'),
    Output('download-link', 'style'),
    Input('generate-report-btn', 'n_clicks'),
    State('report-content-options', 'value'),
    State('additional-comments', 'value'),
    State('stored-data', 'data'),
    prevent_initial_call=True
)
def generate_report_callback(n_clicks, selected_content, comments, data_json):
    if n_clicks is None or data_json is None:
        return ''
    else:
        # Convertir los datos de JSON a DataFrame
        df = pd.read_json(data_json, orient='split')

        # Generar el reporte
        report_file_path = generate_report(df, selected_content, comments)

        # Crear el enlace de descarga
        download_component = html.A(
            "Descargar Reporte",
            href=f"/download/{report_file_path}",
            target="_blank",
            className='btn btn-success'
        )

        style = {'display': 'block'}

        return download_component, style
