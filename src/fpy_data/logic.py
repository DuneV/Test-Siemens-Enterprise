# src/signal_analysis/logic.py

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.signal_analytics import SignalAnalytics  # Asegúrate de importar la clase correctamente


def calculate_signal_parameters(df):
    """
    Calcula los parámetros de la señal utilizando la clase SignalAnalytics.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - signal_params: dict
        Diccionario con los parámetros de la señal.
    """
    # Guardar el DataFrame en un archivo CSV temporal (si es necesario)
    # Si SignalAnalytics puede aceptar un DataFrame directamente, puedes modificar su __init__

    # Crear una instancia de SignalAnalytics
    threshold = 1e-4  # Ajusta el umbral según sea necesario
    signal_analytics = SignalAnalytics(df, threshold)

    # Obtener la frecuencia central
    central_frequency = signal_analytics.frecuenciaCentral()

    # Obtener el ancho de banda
    bandwidth_info = signal_analytics.anchoDeBanda(threshold_db=-3)
    if bandwidth_info is not None:
        bandwidth, freq_low, freq_high = bandwidth_info
    else:
        bandwidth, freq_low, freq_high = None, None, None

    # Obtener la potencia de la señal
    power_mw = signal_analytics.potencia()
    power_dbm = 10 * np.log10(power_mw)

    # Nivel de ruido (se estima fuera del ancho de banda)
    # Podemos usar las frecuencias fuera del ancho de banda para estimar el ruido
    noise_indices = np.where((signal_analytics.frecuency < freq_low) | (signal_analytics.frecuency > freq_high))[0]
    if len(noise_indices) > 0:
        noise_power = np.mean(signal_analytics.linear_mg[noise_indices] ** 2)
        noise_power_dbm = 10 * np.log10(noise_power)
    else:
        noise_power_dbm = None

    # Calcular SNR
    if noise_power_dbm is not None:
        snr = power_dbm - noise_power_dbm
    else:
        snr = None

    # Factor de cresta
    crest_factor = signal_analytics.calculate_crest_factor()

    # Picos espectrales
    peaks_indices = signal_analytics.detect_peaks()
    spectral_peaks = signal_analytics.frecuency[peaks_indices]

    # Frecuencias espurias
    spurious_frequencies = signal_analytics.frecuenciasSpuria()

    # Frecuencias armónicas
    harmonic_frequencies = signal_analytics.detect_harmonics()

    # Tipo de modulación
    modulation_type = signal_analytics.detect_modulation_from_frequency_series()

    # Análisis de ancho de banda de ocupación
    if bandwidth is not None:
        bw_utilization = signal_analytics.determine_bandwidth_utilization(freq_low, freq_high)
    else:
        bw_utilization = None

    # Frecuencia de repetición de pulso (PRF)
    prf = signal_analytics.calculate_prf()

    # Drift de frecuencia
    t, main_frequencies = signal_analytics.detect_main_frequency_changes_from_fft()

    # Tiempo de ocupación
    active_time, total_time, presence_fraction = signal_analytics.detect_signal_presence_in_spectrum()

    # Medición de potencia de canal (ejemplo para el canal principal)
    power_in_band = signal_analytics.calculate_power_in_bandwidth(freq_low, freq_high)

    # Almacenar los parámetros en un diccionario
    signal_params = {
        "Frecuencia Central (MHz)": central_frequency / 1_000_000,
        "Ancho de Banda (MHz)": bandwidth / 1_000_000,
        "Potencia Total (dBm)": round(power_dbm, 2),
        "Nivel de Ruido (dBm)": round(noise_power_dbm, 2) if noise_power_dbm is not None else "N/A",
        "Relación Señal-Ruido (SNR) (dB)": round(snr, 2) if snr is not None else "N/A",
        "Crest Factor": round(crest_factor, 2),
        "Picos Espectrales (MHz)": ', '.join([str(freq / 1_000_000) for freq in spectral_peaks]) if len(spectral_peaks) else "N/A",
        "Frecuencias Espurias (MHz)": ', '.join([str(freq / 1_000_000) for freq, amp in spurious_frequencies]) if len(spurious_frequencies) else "N/A",
        "Frecuencias Armónicas (MHz)": ', '.join([str(freq / 1_000_000) for freq in harmonic_frequencies]) if len(harmonic_frequencies) else "N/A",
        "Tipo de Modulación": modulation_type,
        "Utilización de Ancho de Banda": f"{bw_utilization*100:.2f}%" if bw_utilization is not None else "N/A",
        "Frecuencia de Repetición de Pulso (PRF) (MHz)": prf / 1_000_000 if prf is not None else "N/A",
        "Tiempo de Ocupación (s)": round(active_time, 2),
        "Fracción de Tiempo de Ocupación": f"{presence_fraction*100:.2f}%",
        "Potencia en el Canal (mW)": round(power_in_band, 2),
        # Agrega más parámetros si es necesario
    }

    return signal_params


def generate_signal_spectrum(df):
    """
    Genera una figura de Plotly con el espectro de la señal.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura del espectro de la señal.
    """
    print("Ejecutando generate_signal_spectrum")
    fig = px.line(df, x='frecuency', y='magnitude', title='Espectro de la Señal')
    fig.update_xaxes(title='Frecuencia (Hz)')
    fig.update_yaxes(title='Amplitud (dBm)')
    return fig

def generate_signal_spectrogram(df):
    """
    Genera una figura de Plotly con el espectrograma de la señal (Waterfall display).

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura del espectrograma de la señal.
    """
    # Crear una instancia de SignalAnalytics
    threshold = 1e-4  # Ajusta el umbral según sea necesario
    signal_analytics = SignalAnalytics(df, threshold)

    # Obtener la figura del espectrograma
    fig = signal_analytics.waterfall_display()

    return fig


def generate_inverse_fourier_figure(df):
    """
    Genera una figura de Plotly con la señal en el dominio del tiempo obtenida mediante la Transformada Inversa de Fourier.

    Parameters:
    - df: pandas.DataFrame
        DataFrame con los datos de la señal.

    Returns:
    - fig: plotly.graph_objs._figure.Figure
        Figura de la señal en el dominio del tiempo.
    """
    # Crear una instancia de SignalAnalytics
    threshold = 1e-4  # Ajusta el umbral según sea necesario
    signal_analytics = SignalAnalytics(df, threshold)

    # Obtener la señal recuperada y el vector de tiempo
    señal_recuperada, t = signal_analytics.inverse()

    # Convertir la señal recuperada a dominio real (en caso de que sea compleja)
    señal_recuperada_real = np.real(señal_recuperada)

    # Crear la figura utilizando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=t,
        y=señal_recuperada_real,
        mode='lines',
        name='Señal Recuperada'
    ))

    fig.update_layout(
        title='Señal en el Dominio del Tiempo (Transformada Inversa de Fourier)',
        xaxis_title='Tiempo (s)',
        yaxis_title='Amplitud',
        template='plotly_white'
    )

    return fig
