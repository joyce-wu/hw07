'''
Naotaka Kinoshita, Joyce Wu
SoftDev1 pd7
HW07 -- Do I Know You?
2017-10-05
'''

from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
#secret key created for session specific to computer
app.secret_key = os.urandom(32)
#hardcoded account username and password
username = "bob"
pw = "bye"

@app.route("/")
def hello():
    #checks if computer is already logged in
    print session
    if("username" in session and session.get('username') == username):
        return render_template("welcome.html", username = username)
    #if not, return login template
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    dict = request.form
    #checks to see if username and password is correct
    #returns error page if account information does not match
    if(dict["user"] != username):
        return render_template("error.html", error="bad username")
    if(dict["password"] != pw):
        return render_template("error.html", error="bad password")
    #renders welcome template if account information matches
    else:
        #print session
        session["username"] = username
        #print session
        return render_template("welcome.html", username=username)

@app.route("/logout", methods=["POST"])
def logout():
    #verifies if logout button was clicked
    print request.form
    if(request.form["log"] == "logout"):
        session.pop("username", None) #removes username from session, logging out
        return render_template("login.html") #returns to login page

if __name__ == "__main__":
    app.debug = True
    app.run()
