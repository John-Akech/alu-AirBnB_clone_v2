#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
=======
"""
This is a simple Flask web application.

It defines two routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"

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
<<<<<<< HEAD
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
def about():
    """Route for "/hbnb"."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 426e2ecf714ea63d3944996a4621bdb040eedfc6
