
from flask import Flask

from delivery.ext import config
from delivery.ext import toolbar
from delivery.ext import site


def create_app() -> Flask:
	app = Flask(__name__)
	config.init_app(app)
	toolbar.init_app(app)
	site.init_app(app)
	return app
