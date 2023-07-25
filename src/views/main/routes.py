from flask import Blueprint, render_template
from os import path
from src.models import Term, Subject
from src.config import Config
import json

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder="TEMPLATES_FOLDER")


@main_blueprint.route("/",methods=["GET", "POST"])
def index():
    terms_list = Term.query.limit(3)
    subjects_list = Subject.query.limit(1)
    return render_template("main/index.html", terms_3=terms_list, subjects_3=subjects_list)

@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")
@main_blueprint.route("/dictionary")
def dictionary():
    term_list = Term.query.paginate(per_page=4, max_per_page=100)
    subject_list = Subject.query.limit(1)
    return render_template("main/dictionary.html", terms=term_list, subjects=subject_list)

@main_blueprint.route("/dictionarydetailed/<int:id>")
def dictionary_detailed(id):
    chosen_terms = Term.query.get(id)
    chosen_subjects = Subject.query.get(id)
    return render_template("main/dictionary-detailed.html", detailed_term=chosen_terms, detailed_subject=chosen_subjects)

@main_blueprint.route("/error")
def error():
    return render_template("main/error-page.html")