#!/usr/bin/python3
""" first flask file
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloHBNB():
    """return Hello HBNB! at the main route /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """return Hello HBNB! at the file hbnb route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """return c and the text"""
    CleanText = text.replace('_', ' ')
    return f"C {CleanText}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
