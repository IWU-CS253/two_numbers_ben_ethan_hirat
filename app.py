from flask import Flask, render_template, request


app = Flask(__name__)

OPERATIONS = [
    "+",
    "-",
    "*",
    "/"
]

@app.route("/")
def index():
    return render_template("index.html", operations=OPERATIONS)

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")
    op = request.form.get("op")
    if (op == "+"):
        result = int(num1) + int(num2)
    elif (op == "-"):
        result = int(num1) - int(num2)
    elif (op == "*"):
        result = int(num1) * int(num2)
    elif (op == "/" and num2 != 0):
        result = int(num1) / int(num2)
    return render_template("results.html", result=result)

