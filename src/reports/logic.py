# src/reports/logic.py

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from fpdf import FPDF
import uuid
import numpy as np

# Importar funciones y clases necesarias
from utils.signal_analytics import SignalAnalytics
from signal_analysis.logic import (
    calculate_signal_parameters,
    generate_signal_spectrum,
    generate_signal_spectrogram,
    generate_inverse_fourier_figure  # Importar la nueva función
)
from interferences.logic import detect_interferences, generate_interference_table, generate_interference_spectrum

def get_available_content_options():
    """
    Proporciona las opciones de contenido disponibles para el reporte.

    Returns:
    - options: list of dict
        Lista de opciones para el componente dbc.Checklist.
    """
    options = [
        {'label': 'Parámetros de la Señal', 'value': 'signal_parameters'},
        {'label': 'Gráfico del Espectro', 'value': 'spectrum_graph'},
        {'label': 'Espectrograma', 'value': 'spectrogram'},
        {'label': 'Señal en el Dominio del Tiempo', 'value': 'inverse_fourier'},  # Nueva opción
        {'label': 'Interferencias Detectadas', 'value': 'interferences'},
        # Agregar más opciones según sea necesario
    ]
    return options

def generate_report(df, selected_content, comments):
    """
    Genera un reporte en PDF con el contenido seleccionado.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.
    - selected_content: list of str
        Lista de contenidos seleccionados por el usuario.
    - comments: str
        Comentarios adicionales proporcionados por el usuario.

    Returns:
    - report_file_path: str
        Ruta al archivo PDF generado.
    """
    # Crear una instancia de FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título del reporte
    pdf.cell(200, 10, txt="Reporte de Análisis de Señal", ln=True, align='C')
    pdf.ln(10)

    # Agregar comentarios adicionales
    if comments:
        pdf.multi_cell(0, 10, txt=f"Comentarios adicionales:\n{comments}")
        pdf.ln(10)

    # Crear instancia de SignalAnalytics
    threshold = 1e-4  # Ajusta el umbral según sea necesario
    signal_analytics = SignalAnalytics(df, threshold)

    # Obtener parámetros de la señal
    signal_params = calculate_signal_parameters(df)

    # Incluir el contenido seleccionado
    if 'signal_parameters' in selected_content:
        pdf.cell(0, 10, txt="Parámetros de la Señal:", ln=True)
        pdf.ln(5)
        # Escribir cada parámetro en el PDF
        for key, value in signal_params.items():
            pdf.cell(0, 10, txt=f"{key}: {value}", ln=True)
        pdf.ln(5)

    if 'spectrum_graph' in selected_content:
        # Generar y guardar el gráfico del espectro
        spectrum_fig = generate_signal_spectrum(df)
        spectrum_fig_path = save_figure(spectrum_fig, 'spectrum_graph.png')
        # Insertar el gráfico en el PDF
        pdf.cell(0, 10, txt="Espectro de la Señal:", ln=True)
        pdf.ln(5)
        pdf.image(spectrum_fig_path, w=180)
        pdf.ln(5)

    if 'spectrogram' in selected_content:
        # Generar y guardar el espectrograma
        spectrogram_fig = generate_signal_spectrogram(df)
        spectrogram_fig_path = save_figure(spectrogram_fig, 'spectrogram.png')
        # Insertar el gráfico en el PDF
        pdf.cell(0, 10, txt="Espectrograma de la Señal:", ln=True)
        pdf.ln(5)
        pdf.image(spectrogram_fig_path, w=180)
        pdf.ln(5)

    if 'interferences' in selected_content:
        # Detectar interferencias
        interference_list = detect_interferences(df)
        # Generar gráfico con interferencias marcadas
        interference_fig = generate_interference_spectrum(df, interference_list)
        interference_fig_path = save_figure(interference_fig, 'interference_spectrum.png')
        # Insertar el gráfico en el PDF
        pdf.cell(0, 10, txt="Interferencias Detectadas:", ln=True)
        pdf.ln(5)
        pdf.image(interference_fig_path, w=180)
        pdf.ln(5)
        # Agregar tabla de interferencias
        pdf.cell(0, 10, txt="Detalle de las Interferencias:", ln=True)
        pdf.ln(5)
        interference_table = pd.DataFrame(interference_list)
        # Escribir la tabla en el PDF
        for index, row in interference_table.iterrows():
            pdf.cell(0, 10, txt=f"Frecuencia: {row['Frequency (MHz)']} Hz, Potencia: {row['Power']}", ln=True)
        pdf.ln(5)

    # Agregar más contenido según sea necesario
    if 'inverse_fourier' in selected_content:
        # Generar y guardar la figura de la Transformada Inversa de Fourier
        inverse_fourier_fig = generate_inverse_fourier_figure(df)
        inverse_fourier_fig_path = save_figure(inverse_fourier_fig, 'inverse_fourier.png')
        # Insertar el gráfico en el PDF
        pdf.cell(0, 10, txt="Señal en el Dominio del Tiempo (Transformada Inversa de Fourier):", ln=True)
        pdf.ln(5)
        pdf.image(inverse_fourier_fig_path, w=180)
        pdf.ln(5)

    # Obtener el directorio raíz (un nivel por encima de 'src/')
    current_dir = os.getcwd()
    # Ruta al directorio 'reports' en el nivel raíz
    reports_dir = os.path.join(current_dir, 'reports')
    os.makedirs(reports_dir, exist_ok=True)

    # Generar un nombre único para el archivo
    report_file_name = f"reporte_{uuid.uuid4()}.pdf"
    report_file_path = os.path.join(reports_dir, report_file_name)


    # Guardar el PDF
    pdf.output(report_file_path)

    return report_file_path

def generate_spectrum_figure(df):
    """
    Genera la figura del espectro de la señal utilizando SignalAnalytics.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura del espectro.
    """
    # Usar la función actualizada de generate_signal_spectrum
    fig = generate_signal_spectrum(df)
    return fig

def generate_spectrogram_figure(df):
    """
    Genera la figura del espectrograma de la señal utilizando SignalAnalytics.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura del espectrograma.
    """
    # Usar la función actualizada de generate_signal_spectrogram
    fig = generate_signal_spectrogram(df)
    return fig

def save_figure(fig, filename):
    """
    Guarda una figura de Plotly en un archivo de imagen.

    Parameters:
    - fig: plotly.graph_objs._figure.Figure
        Figura a guardar.
    - filename: str
        Nombre del archivo.

    Returns:
    - filepath: str
        Ruta al archivo guardado.
    """
    filepath = os.path.join('reports', filename)
    os.makedirs('reports', exist_ok=True)
    # Guardar la figura como PNG
    fig.write_image(filepath, format='png')
    return filepath
