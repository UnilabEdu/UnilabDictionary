from flask import Blueprint, render_template
from os import path
from models import Term, Subject
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
    term_list = Term.query.all()
    return render_template("main/dictionary.html", term_list=term_list)

@main_blueprint.route("/dictionarydetailed/")
def dictionary_detailed():
    terms = Term.query.with_entities(Term.eng_word, Term.geo_word, Term.subject, Term.description, Term.example).limit(1)
    subjects = Subject.query.with_entities(Subject.course_link, Subject.internship_link, Subject.name).limit(1)
    return render_template("main/dictionary-detailed.html", terms=terms, subjects=subjects)

@main_blueprint.route("/error")
def error():
    return render_template("main/error-page.html")