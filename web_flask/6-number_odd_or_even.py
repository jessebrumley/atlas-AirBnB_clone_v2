#!/usr/bin/python3

""" Starts a Flash Web Application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(c_text):
    """ Prints C followed by the value of text, replacing _ with spaces """
    return 'C ' + c_text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<py_text>', strict_slashes=False)
def pytext(py_text='is cool'):
    """ Display “Python ”, followed by the value of the text variable,
    replacing underscore _ symbols with a space """
    return 'Python ' + py_text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_integer(n):
    """ display “n is a number” only if n is an integer """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_html(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           parity=parity)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)