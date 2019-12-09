from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import string
import random


def randomPassword(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


project_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/WindowS 10/PycharmProjects/simpleweb/SAppDB.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class users(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(40), primary_key=True, unique=True, nullable=False)
    Password = db.Column(db.String(40), nullable=False)
    Email = db.Column(db.String(40), nullable=False)
    ContactNo = db.Column(db.String(40), nullable=False)
    roles = db.Column(db.String(10),  nullable=False)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        userRole = request.form["userRole"]
        username = request.form["username"]
        login = users.query.filter_by(roles=userRole, Username=username).first()
        if login is not None:
            if userRole == 'Admin':
                return redirect(url_for("dashboard"))
            elif userRole == 'Teacher':
                return redirect(url_for('teacherProfile'))
            elif userRole == 'Student':
                return redirect(url_for('studentProfile'))
            else:
                return redirect(url_for('home'))
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        userRole = request.form["userRole"]
        username = request.form["username"]
        usermail = request.form["usermail"]
        password = randomPassword()
        contact = request.form["contact"]
        registerUser = users(Username=username, Email=usermail, Password=password, roles=userRole, ContactNo=contact)
        db.session.add(registerUser)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("register.html")


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/teacherProfile')
def teacherProfile():
    return render_template('teacherprofile.html')


@app.route('/studentProfile')
def studentProfile():
    return render_template('studentprofile.html')


if __name__ == '__main__':
    db.create_all()
    app.run()
