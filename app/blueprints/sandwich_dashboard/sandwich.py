from flask import Blueprint, render_template, abort
import html
import sys


sandwich_dashboard_bp = Blueprint(
    "sandwich-dashboard", __name__, template_folder="templates"
)


@sandwich_dashboard_bp.route("/sandwich/")
def sandwich() -> html:
    # return render_template("sandwich-dashboard.html")
    abort(501)
