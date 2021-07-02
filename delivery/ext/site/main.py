
from flask import Blueprint, render_template

blueprint = Blueprint("site", __name__)


@blueprint.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@blueprint.route("/about", methods=["GET"])
def about():
	return render_template("about.html")
