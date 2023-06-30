from flask.cli import with_appcontext
from src.extensions import db
from src.models import User, Term
import click


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

    roles = ["admin", "moderator", "member"]
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(username="admin", password="password123", role_id=1)
    admin_user.create()
