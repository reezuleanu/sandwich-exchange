from .components import draw_pie_chart
from dash import html
import sys

sys.path.append("../")
from server.models import Sandwich


def setup_piechart(sandwich: Sandwich, user_owned: int | None = 0) -> html.Div:

    layout = html.Div(
        [draw_pie_chart(sandwich=sandwich, user_owned=user_owned)],
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
    )

    return layout
