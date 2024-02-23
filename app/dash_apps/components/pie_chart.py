from dash import dcc
from plotly import graph_objects as go
import sys

sys.path.append("../")
from server.models import Sandwich


def draw_pie_chart(
    sandwich: Sandwich,
    id: str | None = "",
    height: int | None = 300,
    width: int | None = 300,
    user_owned: int | None = 0,
) -> dcc.Graph:
    """Function which returns a graph of a pie chart showing the total volume of stocks, how many are on sale, how many are owned, and how many
    are owned by the user (if user data provided)

    Args:
        sandwich (Sandwich): sandwich data
        id (str | None, optional): HTML id. Defaults to "".
        height (int | None, optional): CSS height. Defaults to 400.
        width (int | None, optional): CSS width. Defaults to 400.

    Returns:
        dcc.Graph: Returned pie chart graph
    """

    values = [sandwich.on_sale, sandwich.volume - sandwich.on_sale]
    labels = ["Selling", "Already Owned"]

    if user_owned > 0:
        values.append(user_owned)
        labels.append("Owned by you")

    graph = dcc.Graph(
        id=id,
        figure={
            "data": [
                go.Pie(
                    labels=labels,
                    values=values,
                    hole=0.4,
                )
            ],
            "layout": go.Layout(
                title="Stock volume",
                paper_bgcolor="#22252f",
                width=width,
                height=height,
                font={"color": "white"},
            ),
        },
    )

    return graph
