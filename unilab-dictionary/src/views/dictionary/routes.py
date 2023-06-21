from flask import Blueprint, render_template
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "dictionary")
dictionary_blueprint = Blueprint("dictionary", __name__, template_folder="TEMPLATES_FOLDER")


@dictionary_blueprint.route("/dictionary")
def dictionary():
    return render_template("dictionary/dictionary.html")