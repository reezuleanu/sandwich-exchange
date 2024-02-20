from dash import Dash
from dash import html
import sys
from flask import Flask, render_template
from dash_apps.app1 import setup_layout

sys.path.append("../")


app = Flask("flask_server")


app1 = Dash(server=app, url_base_pathname="/dash/sandwiches/")
app1.layout = setup_layout(app1)


@app.route("/")
def index() -> dict:
    return {"respone": "hello!"}


@app.route("/sandwiches/")
def app1() -> html:
    return render_template(
        "index.html", context="Hello There!", context2="This is all rendered by flask"
    )


if __name__ == "__main__":
    app.run(debug=True)
