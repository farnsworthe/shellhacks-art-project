from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    return render_template("results.html")

if __name__ == '__main__':
    app.run(debug=True)