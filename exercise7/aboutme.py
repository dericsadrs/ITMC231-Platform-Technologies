 
#Author          : Deric San ANdres
#Course and Year : 2-BSIT
#Filename        : base.html
#Description     : This is the parent template for child templates home, about and connect
#Honor Code      : I have not given nor received any unathorized help in
#                  completing this exercise. I am also well aware of the 
#                 policies stipulated in the AdNU student handbook


# to use flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

#home page 
def home():
    return render_template("home.html") # to access the home.html

@app.route("/about")
#about page
def about():
    return render_template("about.html") # to access the about.html

@app.route("/connect")
#connect page
def connect():
    return render_template("connect.html") # to access the connect.html