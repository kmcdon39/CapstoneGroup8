from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for


app = Flask(__name__)

@app.route("/")
def getMembers():
    members = 50
    return render_template('club.html', members=members)

if __name__ == "__main__":
    app.run()
