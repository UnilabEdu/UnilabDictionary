from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import User, Term, Role



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

    roles = ["admin", "moderator", "member"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(username="admin", password="es_paroli_shecvalet123", role_id=1)
    admin_user.create()

    click.echo("Creating")
    click.echo("Created")
