from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
import os

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'), static_url_path='/static')

USERNAME = "Janseth Vega"
PASSWORD = "12345678"

queue_data = []

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/get_queue")
def get_queue():
    return jsonify(queue_data)

@app.route("/add_queue", methods=["POST"])
def add_queue():

    data = request.get_json()

    queue_data.append({
        "number": data["number"],
        "status": data["status"]
    })

    return jsonify({
        "success": True
    })

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("dashboard"))

    return render_template("login.html", error="Invalid Username or Password")

@app.route("/delete_queue/<int:index>", methods=["DELETE"])
def delete_queue(index):

    if 0 <= index < len(queue_data):
        queue_data.pop(index)

    return jsonify({"success": True})

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/staff")
def staff():
    return render_template("staff_panel.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)