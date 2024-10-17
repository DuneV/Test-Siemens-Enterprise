# src/app.py

from flask import Flask, send_from_directory
from dash import Dash
import dash_bootstrap_components as dbc
import os

# Inicializar la aplicación Dash con configuraciones
server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

# Establecer el título de la aplicación
app.title = "Análisis de Señales de RF"

# Exponer el servidor Flask subyacente
server = app.server

# Ruta para descargar el reporte
@app.server.route('/download/<path:filename>')
def download_report(filename):
    # Obtener el directorio actual (src/)
    current_dir = os.getcwd()
    # Construir la ruta al directorio 'reports' en el nivel raíz
    reports_dir = os.path.join(current_dir, 'reports')
    # Opcional: imprimir para depuración
    print(f"Attempting to send file from directory: {reports_dir}")
    print(f"Filename requested: {filename}")
    # Enviar el archivo desde el directorio correcto
    return send_from_directory(reports_dir, filename, as_attachment=True)
