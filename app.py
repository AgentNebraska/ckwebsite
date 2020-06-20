from flask import Flask, render_template

app = Flask(__name__)

# need to fix formatting of displayBackground (right now it is in stlye.css)

@app.route("/")
def index():
    displayBackground="Images/bread.jpg"
    backgroundID="homeDisplayBackground"
    centeredText="Fighting waste, feeding people."
    return render_template("index.html", displayBackground=displayBackground, backgroundID=backgroundID, centeredText=centeredText)

@app.route("/ourteam")
def ourteam():
    displayBackground="Images/LTmembers.JPG"
    backgroundID="ourteamDisplayBackground"
    centeredText="Our Team"
    return render_template("ourteam.html", displayBackground=displayBackground, backgroundID=backgroundID, centeredText=centeredText)

@app.route("/ourevents")
def ourevents():
    displayBackground="Images/pizza.jpg"
    backgroundID="homeDisplayBackground"
    centeredText="Our Events"
    return render_template("ourevents.html", displayBackground=displayBackground, backgroundID=backgroundID, centeredText=centeredText)
