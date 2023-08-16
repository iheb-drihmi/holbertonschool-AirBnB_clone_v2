#!/usr/bin/python3
"""Import Modules"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """create a basic page"""
    return 'Hello HBNB!'

"""Entry Point"""
if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
