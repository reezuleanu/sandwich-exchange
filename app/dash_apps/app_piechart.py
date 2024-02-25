from .components import plot_pie_chart
from dash import html, Dash, Input, Output, dcc
import sys
import requests

sys.path.append("../")
from server.models import Sandwich
from blueprints.api_interface import API


def setup_piechart(app: Dash, user_owned: int | None = 0) -> html.Div:

    api = API()

    layout = html.Div(
        [
            dcc.Input(
                id="sandwich_id", value="initial value", style={"display": "none"}
            ),
            dcc.Location(id="url"),
        ],
        style={
            #     "background-color": "#22252f",
            "display": "flex",
            "justify-content": "center",
            #     "align-items": "center",
            #     "border": "white solid 2px",
            #     "border-radius": "20px",
            #     "height": f"{410}px",
            #     "width": f"{410}px",
            #     "margin": "10px",
        },
        id="piechart",
    )

    # get sandwich id from url
    @app.callback(Output("sandwich_id", "value"), [Input("url", "pathname")])
    def set_sandwich_id(url_id: str) -> str:
        sandwich_id = url_id.split("/")[-1]

        return sandwich_id

    # draw plot based on sandwich id
    @app.callback(Output("piechart", "children"), [Input("sandwich_id", "value")])
    def plot_draw(sandwich_id: str) -> dcc.Graph:
        sandwich = api.get_sandwich_by_id(sandwich_id)
        return plot_pie_chart(sandwich)

    return layout
