from flask import Blueprint, render_template, request
from sqlalchemy import or_

from src.models import Term, Subject, TermToSubject

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    terms_list = Term.query.limit(3)
    return render_template("main/index.html", terms=terms_list)


@main_blueprint.route("/dictionary")
def dictionary():
    terms = Term.query
    subject = request.args.get("filter")
    sort = request.args.get("sort")
    search = request.args.get("search")

    if search:
        terms = terms.filter(or_(Term.eng_word.ilike(f"%{search}%"), Term.geo_word.ilike(f"%{search}%")))

    if subject:
        terms = terms.join(TermToSubject).filter(TermToSubject.subjects_id == subject)

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


@main_blueprint.route("/term/<int:id>")
def term_definition(id):
    chosen_term = Term.query.get(id)
    return render_template("main/dictionary_detailed.html", term=chosen_term)


@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")
