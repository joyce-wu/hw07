from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
username = "bob"
pw = "bye"

@app.route("/")
def hello():
    if("username" in session and session["username"] == username):
        return render_template("welcome.html", username = username)
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    dict = request.form
    if(dict["user"] != username):
        return render_template("error.html", error="bad username")
    if(dict["password"] != pw):
        return render_template("error.html", error="bad password")
    else:
        return render_template("welcome.html", username=username)

@app.route("/logout", methods=["POST"])
def logout():
    if(request.form["logout"] == "logout"):
        session.pop("username")
        return #redirect back to root route

if __name__ == "__main__":
    app.debug = True
    app.run()
