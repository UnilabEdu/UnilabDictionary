from flask import Flask, render_template
from flask_admin.menu import MenuLink

from src.models.term import Term, Subject
from src.extensions import db, migrate, login_manager, ckeditor
from src.admin import admin, SecureModelView, UserView, TermView, SubjectView
from src.models import User, Term, Role
from src.config import Config
from src.views import main_blueprint, auth_blueprint
from src.commands import init_db, populate_db

BLUEPRINTS = [main_blueprint, auth_blueprint]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    configure_error_handlers(app)

    return app


def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-CKEditor
    ckeditor.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(TermView(Term, db.session, name="ტერმინები"))
    admin.add_view(SubjectView(Subject, db.session, name="მიმართულებები"))
    admin.add_view(UserView(User, db.session, name="პაროლის შეცვლა"))
    admin.add_link(MenuLink("გამოსვლა", url="/logout", icon_type="fa", icon_value="fa-sign-out"))


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def configure_error_handlers(app):
    @app.errorhandler(Exception)
    def not_found(error):
        return render_template("main/error.html")