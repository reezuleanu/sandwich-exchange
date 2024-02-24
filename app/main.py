from dash import Dash, html, callback, Input, Output
import sys
from flask import Flask, abort
from dash_apps.app_top5 import setup_layout
from blueprints import index_bp, sandwich_dashboard_bp, error_bp
from dash_apps.app_piechart import setup_piechart
from dash_apps.app_candlechart import setup_candlechart
from dash_apps.components import plot_candle_data
import requests

sys.path.append("../")

from server.models import Sandwich, Price_history
from datetime import datetime

# initiate server
app = Flask("Sandwich-Exchange-Server")

# add blueprints
app.register_blueprint(index_bp)  # homepage
app.register_blueprint(sandwich_dashboard_bp)  # sandwich dashboard
app.register_blueprint(error_bp)  # html error handler

# initiate dash apps
dash_top_5 = Dash(server=app, url_base_pathname="/dash/sandwiches/")
dash_piechart = Dash(server=app, url_base_pathname="/dash/piechart/")
dash_candlechart = Dash(server=app, url_base_pathname="/dash/candlechart/")


sand = Sandwich(
    **requests.get("http://127.0.0.1:2727/sandwiches/65da190fce06aadd38ff8eba").json()
)
sand.volume = 2000
sand.on_sale = 1500


dash_piechart.layout = setup_piechart(
    sand,
)

dash_candlechart.layout = setup_candlechart(
    dash_candlechart,
    width=1300,
    height=400,
)


# this takes no arguments, so i can initiate it here
dash_top_5.layout = setup_layout()


# user info page
@app.route("/user/")
def user() -> html:
    abort(501)


if __name__ == "__main__":
    # app.run(host="192.168.0.223", port=80, debug=True)
    app.run(debug=True)
