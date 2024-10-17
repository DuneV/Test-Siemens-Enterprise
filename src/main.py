# src/main.py

from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

from app import app, server  # Importar la aplicación y el servidor

# Importar los layouts de los módulos
from home.layout import layout as home_layout
from signal_analysis.layout import layout as signal_analysis_layout
from interferences.layout import layout as interferences_layout
from reports.layout import layout as reports_layout
from about.layout import layout as about_layout

# Importar los callbacks de los módulos (esto registra los callbacks)
import home.callbacks
import signal_analysis.callbacks
import interferences.callbacks
import reports.callbacks
import about.callbacks



# Definir la barra de navegación
navbar = dbc.Navbar(
    dbc.Container(
        [
            # Logos
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Análisis de Requerimientos de S.T", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
            # Navegación
            dbc.Nav(
                [
                    dbc.NavLink("Inicio", href="/", active="exact"),
                    dbc.NavLink("Análisis", href="/signal-analysis", active="exact"),
                    dbc.NavLink("Interferencias", href="/interferences", active="exact"),
                    dbc.NavLink("Reportes", href="/reports", active="exact"),
                    dbc.NavLink("Acerca de", href="/about", active="exact"),
                ],
                navbar=True,
            ),
        ]
    ),
    className="navbar-custom", 
    dark=True,
)

# Definir el layout de la aplicación
app.layout = html.Div(
    style={'backgroundColor': '#ffffff'},  # Cambiar el color de fondo aquí
    children=[
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='stored-data', storage_type='session'),  # Almacenar datos en la sesión
        navbar,  # Navbar que ya definiste
        html.Div(id='page-content')
    ]
)

# Callback para actualizar el contenido de la página según la URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/' or pathname == '/home':
        return home_layout
    elif pathname == '/signal-analysis':
        return signal_analysis_layout
    elif pathname == '/interferences':
        return interferences_layout
    elif pathname == '/reports':
        return reports_layout
    elif pathname == '/about':
        return about_layout
    else:
        return dbc.Container(
            [                                                                                                                            
                html.H1("404: Página no encontrada", className="text-danger"),
                html.Hr(),
                html.P(f"La ruta {pathname} no existe."),
            ],
            className="py-3",
            style={'backgroundColor': '#f0f8ff'}
        )



if __name__ == '__main__':
    app.run_server(debug=True)
