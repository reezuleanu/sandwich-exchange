from dash import dcc
from plotly import graph_objects as go
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
    """Function which returns a candle graph displaying the sandwich info at the desired time intervals

    Args:
        sandwich (Sandwich): sandwich object containing the data
        id (str | None, optional): Optional html element id. Defaults to "".
        height (int | None, optional): Optional css height. Defaults to 400.
        width (int | None, optional): Optional css width. Defaults to 600.
        intervals (str | None, optional): Optional index intervals. Defaults to "hour".

    Returns:
        dcc.Graph: Dash Graph containing a Candlestick Graph
    """

    # define data conversion function
    match intervals:
        case "quarters":
            intervals = sandwich.price_history.by_quarters()
        case "hour":
            intervals = sandwich.price_history.by_hour()
        case "day":
            intervals = sandwich.price_history.by_day()
        case "week":
            intervals = sandwich.price_history.by_week()

    # define graph with data
    graph = dcc.Graph(
        id=id,
        figure={
            "data": [go.Candlestick(intervals)],
            "layout": go.Layout(
                title=sandwich.name,
                # title="Stock Price History",
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

    return graph
