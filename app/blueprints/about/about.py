from flask import Blueprint, abort
import html

about_bp = Blueprint("about-blueprint", __name__, template_folder="templates")


# TODO implement a "about" page
@about_bp.route("/about/")
def about() -> html:
    abort(501)
