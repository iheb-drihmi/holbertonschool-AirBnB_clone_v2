#!/usr/bin/python3
'''Task 6'''
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    ttext = text.replace('_', ' ')
    return f"C {ttext}"


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def variable_pyth(text="is cool"):
    ttext = text.replace('_', ' ')
    return f"Python {ttext}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_n(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_n_template(n=None):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_odd_or_even(n=None):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
