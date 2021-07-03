
import click
from flask import Flask

from delivery.ext.db import db


def init_app(app: Flask):

	@app.cli.command()
	def create_database():
		"""Command to create the database tables"""
		db.create_all()

	@app.cli.command()
	def list_wish():
		click.echo("wishlist")
