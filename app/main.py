from dash import Dash, html
import sys
from flask import Flask, render_template
from dash_apps.app_top5 import setup_layout
from blueprints import index_bp, sandwich_dashboard_bp, error_bp
from dash_apps.app_piechart import setup_piechart

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


start = datetime(2020, 1, 1)
end = datetime.now()
dash_piechart.layout = setup_piechart(
    Sandwich(
        name="KFC's Double Booster",
        price_history=Price_history.generate_history(start, end),
        volume=2000,
        on_sale=500,
    ),
    user_owned=300,
)


# this takes no arguments, so i can initiate it here
dash_top_5.layout = setup_layout()


# user info page
@app.route("/user/")
def user() -> html:
    return "WIP"


if __name__ == "__main__":
    # app.run(host="192.168.0.223", port=80, debug=True)
    app.run(debug=True)
