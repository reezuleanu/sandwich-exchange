from dash import html, dcc
from plotly import graph_objects as go
from datetime import datetime
import sys

sys.path.append("../")
from server.models import Sandwich


def plot_candle_data(
    sandwich: Sandwich,
    id: str | None = "",
    height: int | None = 400,
    width: int | None = 600,
    intervals: str | None = "hour",
) -> dcc.Graph:

    match intervals:
        case "quarters":
            intervals = sandwich.price_history.by_quarters()
        case "hour":
            intervals = sandwich.price_history.by_hour()

    layout = dcc.Graph(
        id=id,
        figure={
            "data": [go.Candlestick(intervals)],
            "layout": go.Layout(
                title=sandwich.name,
                xaxis=dict(title="Date"),
                yaxis=dict(title="Price"),
                plot_bgcolor="#181a1f",
                paper_bgcolor="#22252f",
                font={"color": "WHITE"},
                height=height,
                width=width,
            ),
        },
    )
    return layout
