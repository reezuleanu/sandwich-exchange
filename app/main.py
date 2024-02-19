from dash import Dash
from dash import html, dcc
from plotly import graph_objs as go
from datetime import datetime
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()


app = Dash(name=__name__)

start = datetime(2020, 1, 1)
end = datetime.now()

data = pdr.get_data_yahoo("GOOG", start, end)
data_tesla = pdr.get_data_yahoo("TSLA", start, end)


app.layout = html.Div(
    [
        html.H1(
            "WELCOME TO THE SANDWICH EXCHANGE",
            style={"text-align": "center"},
        ),
        html.Div(
            "This is a Stock Exchange, but for sandwiches. Neat, huh.",
            style={"text-align": "center"},
        ),
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
                    # title="Google Chart Example",
                    title="Subway Footlong",
                    xaxis=dict(title="Date"),
                    yaxis=dict(title="Price"),
                ),
            },
        ),
        dcc.Graph(
            id="tesla-graph",
            figure={
                "data": [
                    go.Candlestick(
                        x=data_tesla.index,
                        open=data_tesla.Open,
                        high=data_tesla.High,
                        low=data_tesla.Low,
                        close=data_tesla.Close,
                    )
                ],
                "layout": go.Layout(
                    # title="Tesla Chart Example",
                    title="McDonald's McRib",
                    xaxis=dict(title="Date"),
                    yaxis=dict(title="Price"),
                ),
            },
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
