from flask import Flask
from src.extensions import db
from src.config import Config
from src.views import main_blueprint, dictionarydetailed_blueprint, dictionary_blueprint, error_blueprint, about_blueprint
from src.commands import init_db

BLUEPRINTS = [main_blueprint, dictionarydetailed_blueprint, dictionary_blueprint, error_blueprint, about_blueprint ]
COMMANDS = [init_db]

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app

def register_extensions(app):

    db.init_app(app)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)