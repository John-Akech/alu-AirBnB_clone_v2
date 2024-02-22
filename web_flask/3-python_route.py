#!/usr/bin/python3
"""
This is a simple Flask web application.

It defines four routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"
- Route for "/c/<text>" that displays "C <text>" where <text> can be any string
- Route for "/python/(<text>)" that displays "Python <text>" where <text> is a parameter that defaults to "is cool"

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

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
    Route for "/hbnb".
    
    Returns:
        str: A message for the about page.
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    Route for "/c/<text>".
    
    Args:
        text (str): The dynamic part of the URL.
        
    Returns:
        str: A message displaying "C <text>", where <text> is the dynamic part of the URL.
    """
    return "C %s" % text.replace('_', ' ')

@app.route("/python/(<text>)")
def python(text="is cool"):
    """
    Route for "/python/(<text>)".
    
    Args:
        text (str, optional): The dynamic part of the URL, defaults to "is cool".
        
    Returns:
        str: A message displaying "Python <text>", where <text> is the dynamic part of the URL.
    """
    return "Python %s" % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
