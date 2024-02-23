from .components import plot_candle_data
from dash import html, callback, Input, Output, Dash, callback_context
import dash_bootstrap_components as dbc
import sys

sys.path.append("../")
from server.models import Sandwich


def setup_candlechart(
    app: Dash,
    sandwich: Sandwich,
    height: int | None = 350,
    width: int | None = 450,
    intervals: str | None = "hour",
) -> html.Div:

    button_css = {
        "color": "white",
        "border-radius": "5px",
        "background-color": "#22252f",
        "border": "0",
    }

    div = html.Div(
        [
            # html.Div(
            #     sandwich1.name,
            #     style={"align-text": "center", "color": "white"},
            #     id="sandwich-1",
            # ),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            html.Button(
                                "Quarters", style=button_css, id="btn-quarters"
                            ),
                            html.Button("Hour", style=button_css, id="btn-hour"),
                            html.Button("Day", style=button_css, id="btn-day"),
                            html.Button("Week", style=button_css, id="btn-week"),
                        ],
                    )
                ]
            ),
            dbc.Container(
                [
                    plot_candle_data(
                        sandwich,
                        intervals=intervals,
                        height=height,
                        width=width,
                    )
                ],
                id="graph",
            ),
        ],
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
        # id=f"{sandwich.name}",
    )

    @app.callback(
        Output("graph", "children"),
        [
            Input("btn-quarters", "n_clicks"),
            Input("btn-hour", "n_clicks"),
            Input("btn-day", "n_clicks"),
            Input("btn-week", "n_clicks"),
        ],
        prevent_initial_call=True,
    )
    def redraw(clicks_quarters, clicks_hour, clicks_day, clicks_week):
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "btn-quarters":
            intervals = "quarters"
        if button_id == "btn-hour":
            intervals = "hour"
        if button_id == "btn-day":
            intervals = "day"
        if button_id == "btn-week":
            intervals = "week"

        return plot_candle_data(
            sandwich,
            intervals=intervals,
            height=height,
            width=width,
        )

    return div
