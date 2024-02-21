from dash import html, dcc
from plotly import graph_objects as go
from datetime import datetime
import sys

sys.path.append("../")
from server.models import Sandwich


def plot_data(
    sandwich: Sandwich,
    id: str,
    height: int | None = 400,
    width: int | None = 600,
    timeframe: str | None = "hour",
) -> dcc.Graph:

    match timeframe:
        case "quarters":
            timeframe = sandwich.price_history.by_quarters()
        case "hour":
            timeframe = sandwich.price_history.by_hour()

    layout = dcc.Graph(
        id=id,
        figure={
            "data": [go.Candlestick(timeframe)],
            "layout": go.Layout(
                title=sandwich.name,
                xaxis=dict(title="Date"),
                yaxis=dict(title="Price"),
                plot_bgcolor="#424230",
                paper_bgcolor="#424242",
                font={"color": "WHITE"},
                height=height,
                width=width,
            ),
        },
    )
    return layout
