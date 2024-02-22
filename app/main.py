from dash import Dash, html
import dash_bootstrap_components as dbc
import sys
from flask import Flask, render_template
from dash_apps.app_top5 import setup_layout

sys.path.append("../")


app = Flask("flask_server")


app1 = Dash(server=app, url_base_pathname="/dash/sandwiches/")
app1.layout = setup_layout(app1)


@app.route("/")
def index() -> html:
    return render_template("template.html", username="reezuleanu", balance=10000)


@app.route("/user/")
def user() -> html:
    pass


if __name__ == "__main__":
    app.run(host="192.168.0.223", port=80, debug=True)
