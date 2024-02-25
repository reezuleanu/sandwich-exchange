from flask import Blueprint, render_template, abort
import html
import sys
from datetime import datetime
from ..api_interface import API


sys.path.append(".")
from server.models import Sandwich

# blueprint for endpoints relating to sandwich info
sandwich_dashboard_bp = Blueprint(
    "sandwich-dashboard", __name__, template_folder="templates"
)
api = API()


# single sandwich dashboard
@sandwich_dashboard_bp.route("/sandwich/<sandwich_id>/")
def sandwich_dashboard(sandwich_id: str) -> html:
    """Dashboard showing sandwich name, description, pie chart of volume, and stock price history"""

    sandwich = api.get_sandwich_by_id(sandwich_id)

    return render_template(
        "sandwich-dashboard.html",
        sandwich_name=sandwich.name,
        sandwich_description=sandwich.description,
        sandwich_id=sandwich_id,
    )
