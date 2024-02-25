from flask import Blueprint, abort, render_template
import html
import requests
from ..api_interface import API

search_bp = Blueprint("search-blueprint", __name__, template_folder="templates")
api = API()


@search_bp.route("/stonks/")
def get_all_sandwiches() -> html:
    """Display all sandwiches in the database, from most expensive stocks to least expensive stocks"""

    stocks = api.get_all_sandwiches()
    return render_template("stonks.html", stocks=stocks)


@search_bp.route("/search/<sandwich_name>/")
def find_sandwich(sandwich_name: str) -> html:
    """Search the database for a specific sandwich by name

    Args:
        sandwich_name (str): sandwich name (not case sensitive, not exact)

    """

    abort(501)
