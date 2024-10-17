# src/home/logic.py

import pandas as pd
import io
import base64

def read_csv_content(contents, filename):
    """
    Función para leer el contenido del archivo CSV cargado.

    Parameters:
    - contents: str
        Contenido del archivo en formato base64.
    - filename: str
        Nombre del archivo cargado.

    Returns:
    - df: pandas.DataFrame
        DataFrame con los datos del archivo CSV.
    """
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        # Asumimos que es un archivo CSV
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), sep=';')
        return df
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {str(e)}")

    # Código original para leer el CSV (comentado por ahora)
    """
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        # Asumimos que es un archivo CSV
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        return df
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {str(e)}")
    """
