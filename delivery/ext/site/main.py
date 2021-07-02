
from flask import Blueprint
from flask import render_template
from flask import current_app

blueprint = Blueprint("site", __name__)


@blueprint.route("/", methods=["GET"])
def index():
	current_app.logger.debug("index ok")
	return render_template("index.html")


@blueprint.route("/about", methods=["GET"])
def about():
	return render_template("about.html")


@blueprint.route("/restaurants", methods=["GET"])
def restaurants():
	return render_template("restaurants.html")
