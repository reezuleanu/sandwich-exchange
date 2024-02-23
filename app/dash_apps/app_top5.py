from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from plotly import graph_objects as go
from datetime import datetime
from dash_apps.components import plot_candle_data
import sys
from typing import List

sys.path.append("../")
from server.models import Sandwich, Price_history

# ! THESE ARE PARAMETERS FOR GENERATING PRICE HISTORY, TO BE MOVED
start = datetime(2020, 1, 1)
end = datetime.now()


# function to generate sandwiches before i fully implement the database in the app
def generate_sandwiches() -> List[Sandwich]:
    sandwich1 = Sandwich(
        name="KFC's Double Booster",
        price_history=Price_history.generate_history(start, end),
    )

    sandwich2 = Sandwich(
        name="McDonald's McTasty",
        price_history=Price_history.generate_history(start, end),
    )

    sandwich3 = Sandwich(
        name="Wendy's Spicy Chicken Sandwich",
        price_history=Price_history.generate_history(start, end),
    )
    sandwich4 = Sandwich(
        name="Splatoon 3's Crab Trap Sandwich",
        price_history=Price_history.generate_history(start, end),
    )
    sandwich5 = Sandwich(
        name="Skibidi Toilet Sandwich",
        price_history=Price_history.generate_history(start, end),
    )
    return [sandwich1, sandwich2, sandwich3, sandwich4, sandwich5]


# function to generate an appropriate sandwich graph div for the app
def sandwich_div(
    sandwich: Sandwich, height: int | None = 350, width: int | None = 450
) -> html.Div:
    """This function should not be used outside of this module"""

    div = html.Div(
        [
            # html.Div(
            #     sandwich1.name,
            #     style={"align-text": "center", "color": "white"},
            #     id="sandwich-1",
            # ),
            plot_candle_data(sandwich, intervals="day", height=height, width=width),
            html.Div(id=f"{sandwich.name}-redirect-div"),
        ],
        style={
            "background-color": "#22252f",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "border": "white solid 2px",
            "border-radius": "20px",
            "height": f"{height+10}px",
            "width": f"{width+50}px",
            "margin": "10px",
        },
        id=f"{sandwich.name}",
    )

    return div


# sandwich div generation ( first one is special so it's not part of the loop)

divs = []
sandwiches = generate_sandwiches()

divs.append(sandwich_div(sandwiches[0], width=1000))

# ! DISABLED CALLBACKS BECAUSE OF BUG WITH IFRAME
# @callback(
#     Output(f"{sandwiches[0].name}-redirect-div", "children"),
#     [Input(sandwiches[0].name, "n_clicks")],
# )
# def redirect_user(n_clicks):
#     if n_clicks > 0:
#         return dcc.Location(pathname="/", id="redirect")
#     else:
#         return 0


for sandwich in sandwiches[1::]:

    # rest of the sandwiches
    divs.append(sandwich_div(sandwich))

    # @callback(
    #     Output(f"{sandwich.name}-redirect-div", "children"),
    #     [Input(sandwich.name, "n_clicks")],
    # )
    # def redirect_user(n_clicks):
    #     if n_clicks > 0:
    #         return dcc.Location(pathname="/", id="redirect")
    #     else:
    #         return 0


# generate app layout
def setup_layout() -> html.Div:
    """Function which generates the layout for the Top 5 Sandwiches Dash app"""

    layout = html.Div(
        [
            # tried using bootstrap, doesn't really work, maybe because of the iframe
            dbc.Container(
                [
                    dbc.Row(
                        html.H1(
                            "These are the Top 5 Sandwiches on the platform",
                            style={"text-align": "center", "color": "white"},
                        ),
                    ),
                    dbc.Row(
                        [divs[0]],
                        style={"display": "flex", "justify-content": "center"},
                    ),
                    dbc.Row(
                        [divs[1], divs[2]],
                        style={"display": "flex", "justify-content": "center"},
                    ),
                    dbc.Row(
                        [divs[3], divs[4]],
                        style={"display": "flex", "justify-content": "center"},
                    ),
                ]
            )
        ],
        style={
            "font-family": "'Helvetica Neue', Helvetica, Arial, sans-serif",
        },
    )

    return layout
