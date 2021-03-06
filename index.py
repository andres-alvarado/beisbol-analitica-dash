# Dash and bootstrap components
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# App, Navbar
from app import app, server
from navbar import Navbar

# Equipos: layout, callbacks
import equipos.layout as el
import equipos.callbacks as ec

import heatmaps.layout as hl
import heatmaps.callbacks as hc

navbar = Navbar()

content = html.Div([dcc.Location(id="url"), html.Div(id="page-content")])

container = dbc.Container(children=[content], fluid=True )

# Menu callback, set and return
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/equipos":
        return el.layout
    elif pathname == '/heatmaps':
        return hl.layout
    else:
        return "ERROR 404: Page not found!"


app.layout = html.Div(children = [navbar, container] )
