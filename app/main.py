from dash import Dash
from flask import Flask

# blueprint imports
from blueprints import (
    index_bp,
    sandwich_dashboard_bp,
    error_bp,
    search_bp,
    about_bp,
    create_bp,
)

# dash app imports
from dash_apps.app_top5 import setup_layout
from dash_apps.app_piechart import setup_piechart
from dash_apps.app_candlechart import setup_candlechart

import sys

# this is purgatory
sys.path.append("../")

# load .env
from dotenv import load_dotenv
from os import getenv

load_dotenv("../.env")


# initiate server
app = Flask("Sandwich-Exchange-Server")

# add blueprints
app.register_blueprint(index_bp)  # homepage
app.register_blueprint(sandwich_dashboard_bp)  # sandwich dashboard
app.register_blueprint(error_bp)  # html error handler
app.register_blueprint(search_bp)  # everything related to search functionalities
app.register_blueprint(about_bp)  # small page about my vision for the platform
app.register_blueprint(
    create_bp
)  # handler for adding, modifying, and deleting sandwiches

# initiate dash apps
dash_top_5 = Dash(server=app, url_base_pathname="/dash/sandwiches/")
dash_piechart = Dash(server=app, url_base_pathname="/dash/piechart/")
dash_candlechart = Dash(server=app, url_base_pathname="/dash/candlechart/")

# initiate dash app layouts
dash_top_5.layout = setup_layout()

dash_piechart.layout = setup_piechart(
    dash_piechart,
)

dash_candlechart.layout = setup_candlechart(
    dash_candlechart,
    width=1300,
    height=400,
)


# start server
if __name__ == "__main__":
    app.run(host=getenv("FLASK_HOST"), port=int(getenv("FLASK_PORT")), debug=True)
