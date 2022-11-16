import click
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hi")
@app.route("/hello")
def say_hello():
    return "<h1>Hello, Flask!</h1>"

# @app.route("/greet", defaults={'name': 'Programmer'})
@app.route("/greet/", defaults={'name': 'Programmer'})
@app.route("/greet/<name>")
def greet(name):
    return '<h1>Hello, %s!</h1>' % name

# custom flask cli command
@app.cli.command()
# @app.cli.command('say-hello')
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')