#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
=======
"""
This is a simple Flask web application.

It defines four routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"
- Route for "/c/<text>" that displays "C <text>" where <text> can be any string
- Route for "/python/(<text>)" that displays "Python <text>"
- Route for /number/<n> URL.
- Route for /number_template/<n> URL.
- Route for /number_odd_or_even/<n> URL.

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route for the root URL ("/")."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
<<<<<<< HEAD
def hbnb():
    """Displays 'HBNB'"""
=======
def about():
    """Route for /hbnb URL."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
<<<<<<< HEAD
def c(text):
    """Displays 'C' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)
=======
def C(text):
    """Route for /c/<text> URL."""
    return "C %s" % text.replace('_', ' ')
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
<<<<<<< HEAD
    """Displays 'Python' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)
=======
    """Route for /python URL."""
    return "Python %s" % text.replace('_', ' ')
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
<<<<<<< HEAD
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)
=======
    """Route for the /number/<n> URL."""
    return "%d is a number" % n
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
<<<<<<< HEAD
    """Displays an HTML page only if <n> is an integer.

    Displays the value of <n> in the body.
    """
=======
    """Route for the /number_template/<n> URL."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
<<<<<<< HEAD
    """Displays an HTML page only if <n> is an integer.

    States whether <n> is odd or even in the body.
    """
=======
    """Route for the /number_odd_or_even/<n> URL."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
