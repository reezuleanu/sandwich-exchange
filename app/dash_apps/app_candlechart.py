from .components import plot_candle_data
from dash import html, callback, Input, Output, Dash, callback_context, dcc
import dash_bootstrap_components as dbc
import sys
import requests

sys.path.append("../")
from server.models import Sandwich
from blueprints.api_interface import API

"""I spent way to long here and i pity whoever has to review this code. Here, have a sandwich for your troubles: 🥪"""


def setup_candlechart(
    app: Dash,
    height: int | None = 350,
    width: int | None = 450,
    intervals: str | None = "hour",
) -> html.Div:

    api = API()

    # css for interval buttons
    button_css = {
        "color": "white",
        "border-radius": "5px",
        "background-color": "#22252f",
        "border": "1px black solid",
        "cursor": "pointer",
    }

    # app layout
    div = html.Div(
        [
            dcc.Location(id="url"),
            dbc.Container(
                [
                    dbc.Row(
                        [  # interval buttons
                            html.Button(
                                "Quarters", style=button_css, id="btn-quarters"
                            ),
                            html.Button("Hour", style=button_css, id="btn-hour"),
                            html.Button("Day", style=button_css, id="btn-day"),
                            html.Button("Week", style=button_css, id="btn-week"),
                            # place to store the sandwich id from the url
                            dcc.Input(
                                id="sandwich_id",
                                value="initial value",
                                style={"display": "none"},
                            ),
                        ],
                    )
                ]
            ),
            dbc.Container(
                [
                    # here the graph will be drawn
                ],
                id="graph",
            ),
        ],
        # layout css
        style={
            # "background-color": "#22252f",
            "display": "flex",
            "flex-direction": "column",
            # "justify-content": "center",
            "align-items": "center",
            # "border": "white solid 2px",
            # "border-radius": "20px",
            # "height": f"{height+10}px",
            # "width": f"{width+50}px",
            # "margin": "10px",
        },
    )

    # get id from url and put it in a dcc.Input for storage
    @app.callback(Output("sandwich_id", "value"), [Input("url", "pathname")])
    def set_sandwich_id(url_id: str) -> str:
        sandwich_id = url_id.split("/")[-1]

        return sandwich_id

    # if a button clicks or the sandwich id changes, this calls
    @app.callback(
        Output("graph", "children"),
        [
            Input("sandwich_id", "value"),
            Input("btn-quarters", "n_clicks"),
            Input("btn-hour", "n_clicks"),
            Input("btn-day", "n_clicks"),
            Input("btn-week", "n_clicks"),
        ],
        prevent_initial_call=True,
    )
    def redraw(sandwich_id, clicks_quarters, clicks_hour, clicks_day, clicks_week):
        """Countless hours went into perfecting this disaster"""

        # get callback context
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # get sandwich data from api
        sandwich = api.get_sandwich_by_id(sandwich_id)

        # check which button triggered the callback
        if button_id == "btn-quarters":
            intervals = "quarters"
        if button_id == "btn-hour":
            intervals = "hour"
        if button_id == "btn-day":
            intervals = "day"
        if button_id == "btn-week":
            intervals = "week"
        # check if the sandwich id triggered the callback
        if button_id == "sandwich_id":
            intervals = "hour"

        # replot the graph with adjusted data
        return plot_candle_data(
            sandwich,
            intervals=intervals,
            height=height,
            width=width,
        )

    return div
