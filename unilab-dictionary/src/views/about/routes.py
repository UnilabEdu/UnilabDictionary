from flask import Blueprint, render_template
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "about")
about_blueprint = Blueprint("about", __name__, template_folder="TEMPLATES_FOLDER")


@about_blueprint.route("/about")
def about():
    return render_template("about/about.html")