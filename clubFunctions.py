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
        return render_template("studentHome.html", user=user)
    else:
        return render_template("studentHome.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/login.html", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["student"]
        if user != "":
            session["user"] = user
            return redirect(url_for("home"))
        else:
            return render_template("login.html", message="Enter ID")
    else:
        return render_template("login.html")

@app.route("/club.html")
def club():
        if "user" in session:
            members = 50
            user = session["user"]
            return render_template("club.html", user=user, members=members)
        else:
            members = 50
            return render_template("club.html", members=members)

@app.route("/findClubs.html")
def findClubs():
        if "user" in session:
            user = session["user"]
            return render_template("findClubs.html", user=user)
        else:
            return render_template("findClubs.html")

@app.route("/submitClub.html")
def submitClub():
        if "user" in session:
            user = session["user"]
            return render_template("submitClub.html", user=user)
        else:
            return render_template("submitClub.html")
@app.route("/myClubs.html")
def myClubs():
    if "user" in session:
        user = session["user"]
        return render_template("myClubs.html", user=user)
    else:
        return render_template("myClubs.html")

if __name__ == "__main__":
    app.run()
