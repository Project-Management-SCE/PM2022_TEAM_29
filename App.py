from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
import sqlite3
from forms import signupForm

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



if __name__ == '__main__':
    app.run(debug=True)