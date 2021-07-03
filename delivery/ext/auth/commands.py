
import click

from delivery.ext.auth.models import User
from delivery.ext.db import db


def list_users():
	users = User.query.all()
	click.echo(f"list users {users}")


@click.option("--email", "-e")
@click.option("--password", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def created_user(email, password, admin):
	"""creating normal or admin user with --admin or -a flag"""
	user = User(email=email, passwd=password, admin=admin)
	db.session.add(user)
	db.session.commit()

	click.echo(f"User {email} created successfully!")
