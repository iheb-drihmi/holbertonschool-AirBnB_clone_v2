#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


'''Route root URL'''


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display hello World'''
    return "Hello HBNB!"


'''Route for /hbnb'''


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display hello HBNB!'''
    return "HBNB"


'''Route for /hbnb'''


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Display "C" followed by the value of <text>'''
    '''Replace _ with "" in variables'''
    formatText = text.replace('_', ' ')
    return "C {}".format(formatText)


if __name__ == '__main__':
    # start Flask server
    app.run(debug=True, port=5000, host="0.0.0.0")

