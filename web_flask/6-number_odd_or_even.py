#!/usr/bin/python3
""" first flask file
    """
from flask import Flask, render_template


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
    """ return c and the text """
    CleanText = text.replace('_', ' ')
    return "C {}".format(CleanText)


@app.route('/python/', strict_slashes=False)
def python():
    """ return python is cool """
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    """ return python and text """
    CleanText = text.replace('_', ' ')
    return "Python {}".format(CleanText)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ if (n) is int return (n) is a number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ if (n) is int return file html """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ if (n) is int return file html """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
