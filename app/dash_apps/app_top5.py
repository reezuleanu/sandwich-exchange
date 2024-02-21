from dash import Dash, html, dcc
from plotly import graph_objects as go
from datetime import datetime
from dash_apps.components.plot_data import plot_data
import sys

sys.path.append("../")
from server.models import Sandwich, Price_history


def setup_layout(app: Dash) -> html.Div:
    # start = datetime(2020, 1, 1)
    start = datetime(2020, 1, 1)
    end = datetime.now()

    sandwich1 = Sandwich(
        name="KFC's Double Booster",
        price_history=Price_history.generate_history(start, end),
    )

    sandwich2 = Sandwich(
        name="McDonald's McTasty",
        price_history=Price_history.generate_history(start, end),
    )

    div1 = html.Div(
        plot_data(sandwich1, "plot 1", timeframe="quarters", height=350, width=1000),
        style={
            "background-color": "#424242",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "border": "white solid 2px",
            "border-radius": "20px",
            "height": "360px",
            "width": "1100px",
            "margin": "10px",
        },
    )

    div2 = html.Div(
        plot_data(sandwich2, "plot 2", timeframe="quarters", height=350, width=450),
        style={
            "background-color": "#424242",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "border": "white solid 2px",
            "border-radius": "20px",
            "height": "360px",
            "width": "500px",
            "margin": "10px",
        },
    )

    div3 = html.Div(
        plot_data(sandwich2, "plot 3", timeframe="quarters", height=350, width=450),
        style={
            "background-color": "#424242",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "border": "white solid 2px",
            "border-radius": "20px",
            "height": "360px",
            "width": "500px",
            "margin": "10px",
        },
    )

    div4 = html.Div(
        plot_data(sandwich2, "plot 4", timeframe="quarters", height=350, width=450),
        style={
            "background-color": "#424242",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "border": "white solid 2px",
            "border-radius": "20px",
            "height": "360px",
            "width": "500px",
            "margin": "10px",
        },
    )

    div5 = html.Div(
        plot_data(sandwich2, "plot 5", timeframe="quarters", height=350, width=450),
        style={
            "background-color": "#424242",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "border": "white solid 2px",
            "border-radius": "20px",
            "height": "360px",
            "width": "500px",
            "margin": "10px",
        },
    )

    layout = html.Div(
        [
            html.H1(
                "these are the top 5 sandwiches on the platform",
                style={"text-align": "center", "color": "white"},
            ),
            html.Div([div1], style={"display": "flex", "justify-content": "center"}),
            html.Div(
                [div2, div3], style={"display": "flex", "justify-content": "center"}
            ),
            html.Div(
                [div4, div5], style={"display": "flex", "justify-content": "center"}
            ),
        ],
        style={
            # "display": "flex",
            # "justify-content": "center",
            # "align-items": "center",
            # "border": "black solid 2px",
            # "border-radius": "20px",
        },
    )

    return layout
