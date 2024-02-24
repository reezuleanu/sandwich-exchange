from dash import Dash, html, callback, Input, Output
import sys
from flask import Flask, abort

# blueprint imports
from blueprints import index_bp, sandwich_dashboard_bp, error_bp

# dash app imports
from dash_apps.app_top5 import setup_layout
from dash_apps.app_piechart import setup_piechart
from dash_apps.app_candlechart import setup_candlechart

sys.path.append("../")


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
    # app.run(host="192.168.0.223", port=80, debug=True)
    app.run(debug=True)
