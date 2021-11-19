from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import session

app = Flask(__name__)

app.secret_key = "hello"

@app.route("/")
@app.route("/studentHome.html")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("studentHome.html", user=user, login="logout")
    else:
        return render_template("studentHome.html", user=user, login="login")

@app.route("/login.html", methods=["POST", "GET"])
def login():
    global usr
    if request.method == "POST":
        user = request.form["student"]
        session["user"] = user
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/club.html")
def getMembers():
    members = 50
    return render_template('club.html', members=members)

if __name__ == "__main__":
    app.run()
