# src/interferences/logic.py

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import html
from utils.signal_analytics import SignalAnalytics  # Asegúrate de importar la clase correctamente

def detect_interferences(df):
    """
    Detecta interferencias en el espectro de la señal utilizando SignalAnalytics.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - interference_list: list of dict
        Lista de diccionarios con información de las interferencias detectadas.
    """
    # Crear una instancia de SignalAnalytics
    threshold = 1e-4  # Ajusta el umbral según sea necesario
    signal_analytics = SignalAnalytics(df, threshold)

    # Definir los canales a evaluar (puedes ajustar esto según tus necesidades)
    # Por ejemplo, dividimos el espectro en canales de ancho fijo
    total_bandwidth = signal_analytics.frecuency.max() - signal_analytics.frecuency.min()
    num_channels = 10  # Número de canales
    channel_bandwidth = total_bandwidth / num_channels
    channel_centers = np.linspace(
        signal_analytics.frecuency.min() + channel_bandwidth / 2,
        signal_analytics.frecuency.max() - channel_bandwidth / 2,
        num_channels
    )

    # Evaluar interferencias por canal
    interference_results = signal_analytics.evaluate_interference_by_channel(channel_centers, channel_bandwidth)

    interference_list = []
    for center_freq, power in interference_results:
        # Aquí podemos definir un umbral para considerar que hay interferencia
        # Por ejemplo, si la potencia en el canal supera cierto nivel
        interference_threshold = np.mean([p for _, p in interference_results]) + 2 * np.std([p for _, p in interference_results])
        if power > interference_threshold:
            interference = {
                'Frequency (MHz)': center_freq / 1_000_000,
                'Power': power,
                'Type': 'Interferencia detectada'
            }
            interference_list.append(interference)

    return interference_list

def generate_interference_table(interference_list):
    """
    Genera una tabla Dash con las interferencias detectadas.

    Parameters:
    - interference_list: list of dict
        Lista de diccionarios con información de las interferencias detectadas.

    Returns:
    - table: dash_table.DataTable
        Tabla con las interferencias.
    """
    from dash import dash_table

    if not interference_list:
        return html.P("No se detectaron interferencias.")

    df_interferences = pd.DataFrame(interference_list)

    table = dash_table.DataTable(
        data=df_interferences.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df_interferences.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    )

    return table

def generate_interference_spectrum(df, interference_list):
    """
    Genera una figura de Plotly con el espectro de la señal y las interferencias marcadas.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.
    - interference_list: list of dict
        Lista de interferencias detectadas.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura del espectro con interferencias marcadas.
    """
    # Crear una instancia de SignalAnalytics para obtener los datos procesados
    threshold = 1e-4
    signal_analytics = SignalAnalytics(df, threshold)
    frequency = signal_analytics.frecuency
    amplitude_dbm = signal_analytics.magnitude

    fig = go.Figure()
    # Agregar la señal original
    fig.add_trace(go.Scatter(
        x=frequency,
        y=amplitude_dbm,
        mode='lines',
        name='Señal Original'
    ))

    # Marcar las interferencias
    if interference_list:
        frequencies = [interf['Frequency (MHz)'] * 1_000_000 for interf in interference_list]
        #powers = [interf['Power'] for interf in interference_list]
        fig.add_trace(go.Scatter(
            x=frequencies,
            y=amplitude_dbm,
            mode='markers',
            marker=dict(color='red', size=10, symbol='x'),
            name='Interferencias'
        ))

    fig.update_layout(
        title='Espectro de la Señal con Interferencias Marcadas',
        xaxis_title='Frecuencia (Hz)',
        yaxis_title='Amplitud (dBm)'
    )

    return fig


def generate_suavizado_plot(df):
    """
    Genera una figura de Plotly con el espectro de la señal y las interferencias marcadas,
    mostrando tanto la señal original como la señal suavizada.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.
    - interference_list: list of dict
        Lista de interferencias detectadas.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura del espectro con interferencias marcadas.
    """
    # Crear instancias de SignalAnalytics para obtener los datos procesados
    threshold = 1e-4

    # Instancia sin suavizar (señal original)
    signal_analytics_original = SignalAnalytics(df, threshold, suavizar=False)
    frequency = signal_analytics_original.frecuency
    amplitude_dbm_original = signal_analytics_original.magnitude

    # Instancia con suavizar=True (señal suavizada)
    signal_analytics_smoothed = SignalAnalytics(df, threshold, suavizar=True)
    # Convertir la magnitud lineal suavizada a dBm
    amplitude_dbm_smoothed = 20 * np.log10(signal_analytics_smoothed.linear_mg)

    fig = go.Figure()
    # Agregar la señal original
    fig.add_trace(go.Scatter(
        x=frequency,
        y=amplitude_dbm_original,
        mode='lines',
        name='Señal Original'
    ))
    # Agregar la señal suavizada
    fig.add_trace(go.Scatter(
        x=frequency,
        y=amplitude_dbm_smoothed,
        mode='lines',
        name='Señal Suavizada'
    ))

    fig.update_layout(
        title='Espectro de la Señal con Interferencias Marcadas',
        xaxis_title='Frecuencia (Hz)',
        yaxis_title='Amplitud (dBm)'
    )

    return fig


