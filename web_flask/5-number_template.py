#!/usr/bin/python3
"""
This is a simple Flask web application.

It defines four routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"
- Route for "/c/<text>" that displays "C <text>" where <text> can be any string
- Route for "/python/(<text>)" that displays "Python <text>" where <text> is a parameter that defaults to "is cool"
- Route for /number/<n> URL.
- Route for /number_template/<n> URL.


Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Route for the root URL ("/").
    
    Returns:
        str: A message for the index page.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route for the /hbnb URL.
    
    Returns:
        str: A message for the HBNB page.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route for the /c/<text> URL.
    
    Args:
        text (str): Text to display after "C".
    
    Returns:
        str: A message including the text provided in the URL.
    """
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    Route for the /python and /python/<text> URLs.
    
    Args:
        text (str): Text to display after "Python".
    
    Returns:
        str: A message including the text provided in the URL.
    """
    return "Python %s" % text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route for the /number/<n> URL.
    
    Args:
        n (int): Number to display in the URL.
    
    Returns:
        str: A message indicating whether n is a number or not.
    """
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route for the /number_template/<n> URL.
    
    Args:
        n (int): Number to display in the HTML template.
    
    Returns:
        str: Rendered HTML template with the number.
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
