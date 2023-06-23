from flask.cli import with_appcontext
from src.extensions import db
import click
from src.models import term

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating Words")
    populate_db()
    click.echo("Word Created")
