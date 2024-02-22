from dash import Dash, html
import sys
from flask import Flask, render_template
from dash_apps.app_top5 import setup_layout

sys.path.append("../")

# initiate server
app = Flask("Sandwich-Exchange-Server")

# initiate dash apps
app1 = Dash(server=app, url_base_pathname="/dash/sandwiches/")

# this takes no arguments, so i can initiate it here
app1.layout = setup_layout()


# homepage
@app.route("/")
def index() -> html:
    return render_template("index.html", username="reezuleanu", balance=10000)


# user info page
@app.route("/user/")
def user() -> html:
    return "WIP"


if __name__ == "__main__":
    app.run(host="192.168.0.223", port=80, debug=True)
