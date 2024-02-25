from flask import Blueprint, abort, render_template, request, redirect
import html
import sys
from datetime import datetime

sys.path.append("../")
from server.models import Sandwich, Price_history
from ..api_interface import API

create_bp = Blueprint("create-blueprint", __name__, template_folder="templates")
api = API()


@create_bp.route("/create_sandwich/", methods=["POST", "GET"])
def create_sandwich() -> html:
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        sandwich = Sandwich(
            name=str(request.form["sandwich_name"]),
            description=str(request.form["sandwich_description"]),
            # price_history=Price_history.generate_history(
            #     datetime(2020, 1, 1), datetime.now()
            # ),
            volume=int(request.form["total_volume"]),
            on_sale=int(request.form["on_sale"]),
        )

        if api.post_sandwich(sandwich) is True:
            return render_template(
                "create.html", message="Sandwich added successfully", color="green"
            )
        else:
            return render_template(
                "create.html", message="Sandwich could not be added", color="red"
            )


@create_bp.route("/modify_sandwich/", methods=["GET", "POST"])
def modify_sandwich() -> html:
    if request.method == "GET":
        return render_template("modify.html")


# initial delete form endpoint
# here you only enter the sandwich id
# @create_bp.route("/delete_sandwich/")
# def request_delete_sandwich():
#     return render_template("delete.html")


# deletion confirmation endpoint
# here you enter the sandwich name to confirm deletion
# if good, it deletes the sandwich
@create_bp.route("/delete_sandwich/", methods=["GET", "POST"])
def delete_sandwich() -> html:
    sandwich_id = request.args.get("sandwich_id")
    if request.method == "GET":
        if sandwich_id == None:
            return render_template("delete.html")
        sandwich_name = api.get_sandwich_by_id(sandwich_id).name
        return render_template(
            "delete.html",
            sandwich_id=sandwich_id,
            message=f'You are about to delete "{sandwich_name}" from the database. Please retype "{sandwich_name}" to confirm',
            color="red",
        )
    if request.method == "POST":
        sandwich_name = api.get_sandwich_by_id(sandwich_id).name
        if sandwich_name == request.form["confirmation"]:
            if api.delete_sandwich(sandwich_id):
                return render_template(
                    "delete.html",
                    message="Sandwich Deleted Successfully",
                    color="green",
                )
            else:
                return render_template(
                    "delete.html",
                    message="Sandwich could not be deleted : (",
                    color="red",
                )
