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
"""
from flask import Flask
from flask import abort
=======
"""
This is a simple Flask web application.

It defines four routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"
- Route for "/c/<text>" that displays "C <text>" where <text> can be any string
- Route for "/python/(<text>)" that displays "Python <text>"
- Route for the "/number/<n>" URL.

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    """Displays 'Hello HBNB!'."""
=======
    """Route for the root URL ("/")."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
<<<<<<< HEAD
def hbnb():
    """Displays 'HBNB'."""
=======
def display_hbnb():
    """Route for the "/hbnb" URL."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
<<<<<<< HEAD
def c(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
def display_c(text):
    """Route for the "/c/<text>" URL."""
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Route for the "/python/" and "/python/<text>" URLs."""
    return "Python %s" % text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Route for the "/number/<n>" URL."""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
