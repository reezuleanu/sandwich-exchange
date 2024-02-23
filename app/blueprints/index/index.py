from flask import Blueprint, render_template
import html
import sys


sys.path.append(".")
from dash_apps.app_top5 import setup_layout


index_bp = Blueprint("index", __name__, template_folder="templates")


@index_bp.route("/")
def index() -> html:
    return render_template("index.html")
