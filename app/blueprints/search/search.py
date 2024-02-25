from flask import Blueprint, abort, render_template, request
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


@search_bp.route("/search/")
def find_sandwich() -> html:
    """Search the database for a specific sandwich by name

    Args:
        sandwich_name (str): sandwich name (not case sensitive, not exact)

    """
    sandwich_name = request.args.get("search")

    results = api.get_sandwich_by_name(sandwich_name)

    return render_template("search.html", results=results, sandwich_name=sandwich_name)
