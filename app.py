
import views
from flask import Flask


def create_app() -> Flask:
	app = Flask(__name__)
	views.init_app(app=app)
	return app
