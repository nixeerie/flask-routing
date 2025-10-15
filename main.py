from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = datetime.now()
    # kwargs - key word arguments
    return render_template("index.html", today=today)