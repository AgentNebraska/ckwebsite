from flask import Flask, render_template

app = Flask(__name__)

# need to fix formatting of displayBackground (right now it is in stlye.css)

@app.route("/")
def index():
    displayBackground="Images/bread.jpg"
    return render_template("index.html", displayBackground=displayBackground)

@app.route("/ourteam")
def ourteam():
    displayBackground="Images/LTmembers.JPG"
    return render_template("ourteam.html", displayBackground=displayBackground)
