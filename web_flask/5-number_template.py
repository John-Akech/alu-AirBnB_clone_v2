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
def about():
    """
    Route for /hbnb URL.
    
    Returns:
        str: A message for the HBNB page.
    """
    return "HBNB"
    
@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    Route for /c/<text> URL.
    
    Args:
        text (str): Text to display after "C".
    
    Returns:
        str: A message including the text provided in the URL.
    """
    return "C %s" % text.replace('_', ' ')

@app.route("/python")
@app.route("/python/(<text>)")
def python(text="is cool"):
    """
    Route for /python and /python/<text> URLs.
    
    Args:
        text (str, optional): Text to display after "Python". Defaults to "is cool".
    
    Returns:
        str: A message including the text provided in the URL.
    """
    return "Python %s" % text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route for /number/<n> URL.
    
    Args:
        n (int): Number to display in the URL.
    
    Returns:
        str: A message indicating whether n is a number or not.
    """
    return "%d is a number" % n if isinstance(n, int) else None

app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route for /number_template/<n> URL.
    
    Args:
        n (str): Text to be passed to the HTML template.
    
    Returns:
        str: Rendered HTML template.
    """
    return render_template("5-number.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
