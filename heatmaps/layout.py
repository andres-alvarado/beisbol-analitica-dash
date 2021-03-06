# Dash components, html, and dash tables

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt


# Custom dependencies
from heatmaps.specs import object_specs

# Set Container Children Specs
# TODO: Abstract This
for (obj, specs) in object_specs.items():

    if specs["object_type"] == "lov":

        # Set component
        object_specs[specs["container"]]["children"].append(html.Br())
        object_specs[specs["container"]]["children"].append(html.P(specs["P"]))
        object_specs[specs["container"]]["children"].append(
            html.Div(
                dcc.Dropdown(
                    style=specs["style"],
                    id=specs["id"],
                    options=specs["options"],
                    value=specs["value"],
                    clearable=specs["clearable"],
                    placeholder=specs["placeholder"],
                    multi=specs["multi"],
                    searchable=specs["searchable"],
                )
            )
        )

    elif specs["object_type"] == "fig":
        print("GENERATING FIGS FOR HM")
        object_specs[specs["container"]]["children"].append(
            dbc.Col(
                dcc.Graph(id=specs["id"], figure=specs["fig"], config=specs["config"]),
                style={"width": "100%"},
            )
        )
        print("DONE GENERATING FIGS FOR HM")



container_control = dbc.Card(
    children=[
        dbc.CardHeader(object_specs["container_control"]["header"]),
         dbc.CardBody(children=object_specs["container_control"]["children"]),
    ]
)

container_heatmaps = dbc.Card(
    children=[
        dbc.CardHeader(object_specs["container_heatmaps"]["header"]),
        dbc.CardBody(
            children=dbc.Row(
                children=object_specs["container_heatmaps"]["children"]
            )
        )
    ],
    style={"width": "100%"},
)

layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(children=[html.Br()]),
        dbc.Row(
            children=[
                dbc.Col(container_control, width=2),
                dbc.Col(children=[container_heatmaps]),
            ]
        ),
    ],
)
