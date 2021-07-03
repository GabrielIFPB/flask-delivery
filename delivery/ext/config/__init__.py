
from flask import Flask


DATABASE_NAME = 'db.sqlite'


def init_app(app: Flask):
	app.config["SECRET_KEY"] = "SECRET_KEY"
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///../../{DATABASE_NAME}'

	if app.debug:
		app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
		app.config["DEBUG_TB_PROFILER_ENABLED"] = True
		app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

