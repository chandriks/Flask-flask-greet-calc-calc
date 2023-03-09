from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """
        Adding a and b and return the sum
    """
    a = int(request.args.get("a", "Not found"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route("/sub")
def subtraction():
    """
    subtracting b from a and return the difference
    """
    a = int(request.args.get("a", "Not found"))
    b = int(request.args.get("b", "Not found"))
    return str(sub(a,b))

@app.route("/mult")
def muliply():
    """
    Multiple a and b and return the product
    """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a,b))

@app.route("/div")
def divide():
    """
    Divide a by b and return the result
    """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(div(a,b))

