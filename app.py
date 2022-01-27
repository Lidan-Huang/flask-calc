# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def add_result():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(add(a, b))

@app.get("/sub")
def sub_result():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(sub(a, b))

@app.get("/mult")
def mult_result():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(mult(a, b))

@app.get("/div")
def div_result():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(div(a, b))


