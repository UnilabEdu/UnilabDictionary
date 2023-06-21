from flask import Blueprint, render_template
from os import path
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "dictionarydetailed")
dictionarydetailed_blueprint = Blueprint("dictionarydetailed", __name__, template_folder="TEMPLATES_FOLDER")


@dictionarydetailed_blueprint.route("/dictionarydetailed")
def dictionary_detailed():
    return render_template("dictionary-detailed/dictionary-detailed.html")