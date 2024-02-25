from flask import Blueprint, render_template
import html

# blueprint for handling errors
error_bp = Blueprint("error handler", __name__, template_folder="templates")


@error_bp.app_errorhandler(404)
def not_found(e) -> html:
    message = "You have reached the world's edge. None but devils play past here... Turn back."
    image = (
        "https://i.pinimg.com/originals/b7/2d/d0/b72dd05180817700dd6d7558ca653138.gif"
    )
    return render_template("error.html", error_code=404, message=message, image=image)


@error_bp.app_errorhandler(501)
def not_implemented(e) -> html:
    message = (
        "This feature is not implemented yet, so there's nothing to see here friend!"
    )
    image = "https://miro.medium.com/v2/resize:fit:562/1*FOD8mNvBg7Np8qsdWZPVPg.gif"
    return render_template(
        "error.html",
        error_code=501,
        message=message,
        image=image,
    )
