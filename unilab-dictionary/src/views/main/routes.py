from flask import Blueprint, render_template
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder="TEMPLATES_FOLDER")


@main_blueprint.route("/")
def index():
    return render_template("main/index.html")