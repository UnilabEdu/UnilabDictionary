from flask import Blueprint, render_template
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "error")
error_blueprint = Blueprint("error", __name__, template_folder="TEMPLATES_FOLDER")


@error_blueprint.route("/error")
def error():
    return render_template("error/error-page.html")
