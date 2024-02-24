from flask import Blueprint, render_template, abort
import html
import sys
from datetime import datetime
import requests


sys.path.append(".")
from server.models import Sandwich

# blueprint for endpoints relating to sandwich info
sandwich_dashboard_bp = Blueprint(
    "sandwich-dashboard", __name__, template_folder="templates"
)


# single sandwich dashboard
@sandwich_dashboard_bp.route("/sandwich/<sandwich_id>/")
def sandwich_dashboard(sandwich_id: str) -> html:
    """Dashboard showing sandwich name, description, pie chart of volume, and stock price history"""

    sandwich = Sandwich(
        **requests.get(f"http://127.0.0.1:2727/sandwiches/{sandwich_id}").json()
    )

    return render_template(
        "sandwich-dashboard.html",
        sandwich_name=sandwich.name,
        sandwich_description=sandwich.description,
        sandwich_id=sandwich_id,
    )


@sandwich_dashboard_bp.route("/sandwiches/")
def sandwich_list() -> html:
    """List all sandwiches in a list"""

    abort(501)
