#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
=======
"""
This is a simple Flask web application.

It defines four routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"
- Route for "/c/<text>" that displays "C <text>" where <text> can be any string
- Route for "/python/(<text>)" that displays "Python <text>"

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""

>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
=======
def index():
    """Route for the root URL ("/")."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """Displays 'HBNB'."""
=======
    """Route for "/hbnb"."""
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
<<<<<<< HEAD
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
    """Route for "/c/<text>"."""
    return "C %s" % text.replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """Route for "/python/<text>"."""
    return "Python %s" % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
