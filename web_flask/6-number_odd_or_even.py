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
- Route for /number_odd_or_even/<n> URL.

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
        str: Message for the about page.
    """
    return "HBNB"
    
@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    Route for /c/<text> URL.
    
    Args:
        text (str): Text parameter passed in the URL.
    
    Returns:
        str: Message with "C " followed by the value of the text variable.
    """
    return "C %s" % text.replace('_', ' ')

@app.route("/python")
@app.route("/python/(<text>)")
def python(text = "is cool"):
    """
    Route for /python URL.
    
    Args:
        text (str, optional): Text parameter passed in the URL. Defaults to "is cool".
    
    Returns:
        str: Message with "Python " followed by the value of the text variable.
    """
    return "Python %s" % text.replace('_', ' ')
    
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route for /number/<n> URL.
    
    Args:
        n (int): Integer parameter passed in the URL.
    
    Returns:
        str: Message indicating that the passed number is a number.
    """
    return "%d is a number" % n

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route for /number_template/<n> URL.
    
    Args:
        n (int): Integer parameter passed in the URL.
    
    Returns:
        str: Rendered HTML template with the provided number.
    """
    return render_template("5-number.html")

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Route for /number_odd_or_even/<n> URL.
    
    Args:
        n (int): Integer parameter passed in the URL.
    
    Returns:
        str: Rendered HTML template with information about whether the number is odd or even.
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
