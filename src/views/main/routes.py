from flask import Blueprint, render_template, request
from os import path
from src.models import Term, Subject, TermToSubject
from src.config import Config
from sqlalchemy import or_
import json

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder="TEMPLATES_FOLDER")


@main_blueprint.route("/",methods=["GET", "POST"])
def index():
    terms_list = Term.query.limit(3)
    return render_template("main/index.html", terms_3=terms_list)

@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")
@main_blueprint.route("/dictionary")
def dictionary():
    terms = Term.query
    subject = request.args.get("filter")
    sort = request.args.get("sort")
    search = request.args.get("search")

    if search:
        terms = terms.filter(or_(Term.eng_word.ilike(search), Term.geo_word==search))

    if subject:
        terms = terms.join(TermToSubject).filter(TermToSubject.subjects_id==subject)

    if sort:

        if sort == "asc":
            terms = terms.order_by(Term.geo_word.asc())

        elif sort == "desc":
            terms = terms.order_by(Term.geo_word.desc())

        elif sort == "newest":
            terms = terms.order_by(Term.id.desc())

        elif sort == "oldest":
            terms = terms.order_by(Term.id.asc())

    terms = terms.paginate(per_page=4, max_per_page=100)

    subject_list = Subject.query.all()

    return render_template("main/dictionary.html", terms=terms, subjects=subject_list)

@main_blueprint.route("/dictionarydetailed/<int:id>")
def dictionary_detailed(id):
    chosen_terms = Term.query.get(id)
    chosen_subjects = Subject.query.get(id)
    return render_template("main/dictionary-detailed.html", detailed_term=chosen_terms, detailed_subject=chosen_subjects)

@main_blueprint.route("/error")
def error():
    return render_template("main/error-page.html")