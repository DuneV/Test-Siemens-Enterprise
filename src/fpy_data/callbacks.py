# src/fpy_data/callback.py

from dash import Input, Output, State, html  # Asegúrate de importar 'html' aquí
from dash import callback

@callback(
    Output("fpy-modal", "is_open"),
    [Input("fpy-button", "n_clicks"), Input("modal-submit-button", "n_clicks")],
    [State("fpy-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# Callback para actualizar la tabla 
@callback(
    Output("filtered-table", "children"),
    [
        Input("fiscal-year-dropdown", "value"),
        Input("month-dropdown", "value"),
        Input("production-line-dropdown", "value"),
        Input("tested-units-input", "value"),
        Input("failed-units-input", "value"),
    ]
)
def update_table(fy, month, production_line, tested_units, failed_units):
    # Datos reales 
    rows = [
        html.Tr([html.Td(fy or "N/A"), html.Td(month or "N/A"), html.Td(tested_units or "N/A"), html.Td(failed_units or "N/A")])
    ]
    return [  # Thread valido
        html.Thead(html.Tr([html.Th("FY"), html.Th("Month"), html.Th("Tested Units"), html.Th("Failed Units")])),
        html.Tbody(rows)
    ]
