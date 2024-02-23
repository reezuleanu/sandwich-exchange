from dash import Dash, html
import sys
from flask import Flask, render_template
from dash_apps.app_top5 import setup_layout
from blueprints import index_bp, sandwich_dashboard_bp, error_bp

sys.path.append("../")

# initiate server
app = Flask("Sandwich-Exchange-Server")

# add blueprints
app.register_blueprint(index_bp)  # homepage
app.register_blueprint(sandwich_dashboard_bp)  # sandwich dashboard
app.register_blueprint(error_bp)  # html error handler

# initiate dash apps
dash_top_5 = Dash(server=app, url_base_pathname="/dash/sandwiches/")

# this takes no arguments, so i can initiate it here
dash_top_5.layout = setup_layout()


# user info page
@app.route("/user/")
def user() -> html:
    return "WIP"


if __name__ == "__main__":
    # app.run(host="192.168.0.223", port=80, debug=True)
    app.run(debug=True)
