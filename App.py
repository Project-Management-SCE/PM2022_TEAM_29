from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
import sqlite3
from forms import signupForm, SignOutForm, LoginForm

app = Flask(__name__)

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_Giving1.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (username TEXT PRIMARY KEY NOT NULL, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `organization` (username TEXT PRIMARY KEY NOT NULL, password TEXT, age INTEGER, location TEXT, phone TEXT, name TEXT, maxvol TEXT, rating TEXT, numvol TEXT, donation TEXT, hobby TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `volunteer` (username TEXT PRIMARY KEY NOT NULL, password TEXT, age INTEGER, location TEXT, phone TEXT, name TEXT, hour INTEGER, hobby TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `hours` (orgname TEXT NOT NULL,volname TEXT NOT NULL, hour INTEGER, PRIMARY KEY(orgname,volname)) ")
Database()
app.config['SECRET_KEY'] = 'Sujood'
import json
import os
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Sujood'

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    Database()
    form = signupForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        name = form.name.data
        age = form.age.data
        location = form.location.data
        phone = form.phone.data
        hour = form.hour.data
        hobby = form.hobby.data
        cursor.execute("SELECT * FROM `volunteer` WHERE `username` = ?", (username,))
        if cursor.fetchone() is not None:
            flash("username already exist")
            return render_template('register.html', form=form)
        else:
            insert_volunteer(str(username), str(password), str(name), str(age), str(location), str(phone), str(hobby))
            cursor.close()
            conn.close()
    flash("successfully created!")
    return render_template('register.html', form=form)


def insert_volunteer(username, password, age, location, phone, name, hobby):
    try:
        cursor.execute("INSERT INTO `volunteer` (username, password, age, location, phone, name, hobby) VALUES(?, ?, ?,?,?,?,?)",
                       (username, password, age, location, phone, name, hobby))
        conn.commit()
    except ValueError:
        print(ValueError)

@app.route('/volunteer')
def volunteer():
    return redirect(url_for('volunteerPage'))

@app.route('/volunteerPage')
def volunteerPage():
    return render_template('volunteer.html')

@app.route('/uservolunteer',methods=['GET', 'POST'])
def uservolunteer():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logout"))
    return render_template('volunteer.html', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    Database()
    form = LoginForm()
    cursor.execute("SELECT * FROM `volunteer` WHERE `username` = ? and `password` = ?",
                   (form.username.data, form.password.data))
    # if form.validate_on_submit():
    if cursor.fetchone() is not None:
        session["uservol"] = form.username.data
        return redirect(url_for("uservolunteer"))
    else:
        return render_template('login.html', form=form, us="Not Exist")
    # else:
    #     if "user" in session:
    #         return redirect(url_for("uservolunteer"))
    #     return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    session.pop("uservol", None)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)