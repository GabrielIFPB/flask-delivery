
from flask import Flask
from delivery import views


def create_app() -> Flask:
	app = Flask(__name__)
	views.init_app(app=app)
	return app
