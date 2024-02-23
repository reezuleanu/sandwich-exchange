from flask import Blueprint, render_template, abort
import html
import sys


sandwich_dashboard_bp = Blueprint(
    "sandwich-dashboard", __name__, template_folder="templates"
)


@sandwich_dashboard_bp.route("/sandwich/")
def sandwich() -> html:
    """Dashboard showing sandwich name, description, pie chart of volume, and stock price history"""

    return render_template("sandwich-dashboard.html")
