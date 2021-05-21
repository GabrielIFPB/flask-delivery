
from flask import Flask


def init_app(app: Flask):

	@app.route('/')
	def index():
		return '<h1>Hello World!!!</h1>'

	@app.route('/about')
	def about():
		return '<h1>About</h1>'
