from flask import Blueprint, render_template
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder="TEMPLATES_FOLDER")


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("main/index.html")

@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")

@main_blueprint.route("/dictionary")
def dictionary():
    return render_template("main/dictionary.html")

@main_blueprint.route("/dictionarydetailed")
def dictionary_detailed():
    return render_template("main/dictionary-detailed.html")

@main_blueprint.route("/error")
def error():
    return render_template("main/error-page.html")