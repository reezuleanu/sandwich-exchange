from flask import Blueprint, render_template, abort
import html
import sys
from datetime import datetime


sys.path.append(".")
from server.models import Sandwich, Price_history

sandwich_dashboard_bp = Blueprint(
    "sandwich-dashboard", __name__, template_folder="templates"
)


start = datetime(2020, 1, 1)
end = datetime.now()
sandwich1 = Sandwich(
    name="KFC's Double Booster",
    price_history=Price_history.generate_history(start, end),
    volume=2000,
    on_sale=500,
    description="Când ai chef de pui #pebune, dar ți-e și super poftă de ceva nepicant, alegi KFC Dublu Booster. 2 bucăți de pulpă de pui nepicante, 2 felii de brânză Cheddar, castraveți murați, sos burger și ketchup dulce, toate puse într-o chiflă pufoasă. ",
)


@sandwich_dashboard_bp.route("/sandwich/")
def sandwich() -> html:
    """Dashboard showing sandwich name, description, pie chart of volume, and stock price history"""

    sandwich_name = sandwich1.name
    sandwich_description = sandwich1.description

    return render_template(
        "sandwich-dashboard.html",
        sandwich_name=sandwich_name,
        sandwich_description=sandwich_description,
    )
