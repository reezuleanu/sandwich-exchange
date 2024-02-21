from dash import Dash, html, dcc
from plotly import graph_objects as go
from datetime import datetime
from pandas_datareader import data as pdr
import yfinance as yf

import sys

sys.path.append("../")
from server.models import Sandwich, Price_history


def setup_layout(app: Dash) -> html.Div:
    # start = datetime(2020, 1, 1)
    start = datetime(2020, 1, 1)
    end = datetime.now()

    yf.pdr_override()

    # data = pdr.get_data_yahoo("GOOG", start, end)

    sandwich = Sandwich(
        name="KFC's Double Booster",
        price_history=Price_history.generate_history(start, end),
    )

    layout = html.Div(
        [
            dcc.Graph(
                id="google-graph",
                figure={
                    "data": [go.Candlestick(sandwich.price_history.by_hour())],
                    "layout": go.Layout(
                        title=sandwich.name,
                        xaxis=dict(title="Date"),
                        yaxis=dict(title="Price"),
                        plot_bgcolor="#424230",
                        # paper_bgcolor="#424242",
                        # font={"color": "WHITE"},
                        height=400,
                        width=700,
                    ),
                },
                style={"margin-left": "25vw"},
            ),
        ],
        style={
            "background-color": "blue",
            "border-radius": "20px",
            "margin-top": "25vh",
        },
    )

    return layout
