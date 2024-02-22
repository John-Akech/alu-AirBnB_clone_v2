#!/usr/bin/python3
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
    Route for the "/hbnb" URL.
    
    Returns:
        str: A message for the about page.
    """
    return "HBNB"
    
@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    Route for the "/c/<text>" URL.
    
    Args:
        text (str): The text to display after "C ".
    
    Returns:
        str: A message for the "C" page with the provided text.
    """
    return "C %s" % text.replace('_', ' ')

@app.route("/python")
@app.route("/python/(<text>)", strict_slashes=False)
def python(text="is cool"):
    """
    Route for the "/python" and "/python/(<text>)" URLs.
    
    Args:
        text (str): The text to display after "Python ".
    
    Returns:
        str: A message for the "Python" page with the provided text.
    """
    return "Python %s" % text.replace('_', ' ')

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """
    Route for the "/number/<n>" URL.
    
    Args:
        n (str): The number to check.
    
    Returns:
        str: A message indicating whether the provided value is a number.
            If it's a number, it returns "n is a number"; otherwise, it returns None.
    """
    if type(n) == int:
        return "n is a number"
    else:
        return None

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
