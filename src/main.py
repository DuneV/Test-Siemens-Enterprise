# src/main.py

from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

from app import app, server  # Importar la aplicación y el servidor

# Importar los layouts de los módulos
from home.layout import layout as home_layout
from fpy_data.layout import layout as fpy_data_layout
from interferences.layout import layout as interferences_layout
from reports.layout import layout as reports_layout
from about.layout import layout as about_layout

# Importar los callbacks de los módulos (esto registra los callbacks)
import home.callbacks
import fpy_data.callbacks
import interferences.callbacks
import reports.callbacks
import about.callbacks

# Definición de iconos
# (CAMDBIAR NOMBRE)

# icon_inbox = ""
# icon_analitics = ""
# icon_inter = ""
# icon_report = ""

# Definir la barra de navegación
navbar = dbc.Navbar(
    dbc.Container(
        [
            # Logos
            dbc.Row(
            [
                dbc.Col(dbc.NavbarBrand(html.Img(src = "/assets/resource_n1.png", height= "30px"), external_link=True,href="https://www.siemens-energy.com/co/es/home.html"), align="center"),
                # dbc.Col(html.H2("Siemens Quality Hub", className = "ml-2"), align="center"),

            ],
        ),
            # Navegación
                dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Img(src="/assets/icons/flash.png", height="20px", style={'margin-right': '10px'}),  
                        "Home"
                    ], 
                    href="/", active="exact", className="nav-link-custom"
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/icons/flash.png", height="20px", style={'margin-right': '10px'}),  
                        "FPY Data"
                    ], 
                    href="/fpy_data", active="exact", className="nav-link-custom"
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/icons/flash.png", height="20px", style={'margin-right': '10px'}),  
                        "KPI's Module DT"
                    ], 
                    href="/interferences", active="exact", className="nav-link-custom"
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/icons/flash.png", height="20px", style={'margin-right': '10px'}),  
                        "Report"
                    ], 
                    href="/reports", active="exact", className="nav-link-custom"
                ),
                dbc.NavLink(
                    [
                        html.Img(src="/assets/icons/flash.png", height="20px", style={'margin-right': '10px'}),  
                        "About"
                    ], 
                    href="/about", active="exact", className="nav-link-custom"
                ),
            ],
            className="me-auto", 
            navbar=True,
        ),
        ]
    ),
    className="navbar-custom", 
    dark=True,
)

# Definir el layout de la aplicación
app.layout =  html.Div(
    style={
        'backgroundImage': 'url("/assets/placeholder2.jpg")',  # Cambia la ruta a tu imagen
        'backgroundSize': 'cover',  # Asegúrate de que la imagen cubra toda el área
        'backgroundPosition': 'center',  # Centra la imagen
        'height': '100vh',  # Altura de la ventana del navegadord
        'color': '#ffffff'  # Cambia el color del texto si es necesario
    },
    children=[
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='stored-data', storage_type='session'),  # Almacenar datos en la sesión
        navbar,  # Navbar que ya definiste
        html.Div(id='page-content')  # Mantener el contenedor del contenido de la página
    ]
)

# Callback para actualizar el contenido de la página según la URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/' or pathname == '/home':
        return home_layout
    elif pathname == '/fpy_data':
        return fpy_data_layout
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
