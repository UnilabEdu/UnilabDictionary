from flask import Flask
from flask_admin.contrib.sqla import ModelView

from src.models.term import Term, Subject
from src.extensions import db, migrate
from src.admin import admin
from src.config import Config
from src.views import main_blueprint
from src.commands import init_db

BLUEPRINTS = [main_blueprint]
COMMANDS = [init_db]

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    admin.init_app(app)
    admin.add_view(ModelView(Term, db.session))
    admin.add_view(ModelView(Subject, db.session))

    migrate.init_app(app, db)


    return app

def register_extensions(app):

    db.init_app(app)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)