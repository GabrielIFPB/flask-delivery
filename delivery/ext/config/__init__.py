
from flask import Flask


def init_app(app: Flask):
	app.config["SECRET_KEY"] = "SECRET_KEY"

	if app.debug:
		app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
		app.config["DEBUG_TB_PROFILER_ENABLED"] = True

