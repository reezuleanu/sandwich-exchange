from dash import Dash, html, dcc
from plotly import graph_objects as go
from datetime import datetime
from pandas_datareader import data as pdr
import yfinance as yf


def setup_layout(app: Dash) -> html.Div:
    start = datetime(2020, 1, 1)
    end = datetime.now()

    yf.pdr_override()

    data = pdr.get_data_yahoo("GOOG", start, end)

    layout = html.Div(
        [
            dcc.Graph(
                id="google-graph",
                figure={
                    "data": [
                        go.Candlestick(
                            x=data.index,
                            open=data.Open,
                            high=data.High,
                            low=data.Low,
                            close=data.Close,
                        )
                    ],
                    "layout": go.Layout(
                        title="Subway Footlong",
                        xaxis=dict(title="Date"),
                        yaxis=dict(title="Price"),
                        plot_bgcolor="#424230",
                        # paper_bgcolor="#424242",
                        # font={"color": "WHITE"},
                        height=400,
                        width=700,
                    ),
                },
            ),
        ],
    )

    return layout
