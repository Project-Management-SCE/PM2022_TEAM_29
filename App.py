from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
import sqlite3
from forms import signupForm, SignOutForm, LoginForm, signupFormOrg, DeleteVolunteerForm, DeleteOrganizationForm, DeleteFieldForm, UpdateDonationForm

app = Flask(__name__)

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_Giving.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (username TEXT PRIMARY KEY NOT NULL, password TEXT, donation TEXT)")
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

@app.route('/registerOrg', methods=['GET', 'POST'])
def registerOrg():
    Database()
    form = signupFormOrg()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        name = form.name.data
        age = form.age.data
        location = form.location.data
        phone = form.phone.data
        maxvol = form.maxvol.data
        hobby = form.hobby.data
        cursor.execute("SELECT * FROM `organization` WHERE `username` = ?", (username,))
        if cursor.fetchone() is not None:
            flash("username already exist")
            return render_template('registerOrg.html', form=form)
        else:
            insert_organization(str(username), str(password), str(name), str(age), str(location), str(phone), str(maxvol), str(hobby))
            cursor.close()
            conn.close()
    flash("successfully created!")
    return render_template('registerOrg.html', form=form)
def insert_organization(username, password, age, location, phone, name, maxvol, hobby):
    try:
        cursor.execute("INSERT INTO `organization` (username, password, age, location, phone, name, maxvol, hobby) VALUES(?, ?, ?, ?,?,?,?,?)",
                       (username, password, age, location, phone, name, maxvol, hobby))
        conn.commit()
    except ValueError:
        print(ValueError)
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



@app.route('/loginOrg',methods=['GET', 'POST'])
def loginOrg():
    Database()
    form = LoginForm()
    cursor.execute("SELECT * FROM `organization` WHERE `username` = ? and `password` = ?",
                   (form.username.data, form.password.data))
    # if form.validate_on_submit():
    if cursor.fetchone() is not None:
        session["userorg"] = form.username.data
        return redirect(url_for("useror"))
    else:
        return render_template('loginOrg.html', form=form, us="Not Exist")
    # else:
    #     if "user" in session:
    #         return redirect(url_for("userorg"))
    #     return render_template('loginOrg.html', form=form)


@app.route('/useror',methods=['GET', 'POST'])
def useror():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logoutorganization"))
    return render_template('organization.html', form=form)

@app.route('/loginAdmin',methods=['GET', 'POST'])
def loginAdmin():
    Database()
    form = LoginForm()
    cursor.execute("SELECT * FROM `admin` WHERE `username` = ? and `password` = ?",
                   (form.username.data, form.password.data))
    # if form.validate_on_submit():
    if cursor.fetchone() is not None:
        session["useradm"] = form.username.data
        return redirect(url_for("useradmin"))
    else:
        return render_template('loginAdmin.html', form=form, us="Not Exist")
    # else:
    #     if "user" in session:
    #         return redirect(url_for("useradmin"))
    #     return render_template('loginAdmin.html', form=form)

@app.route('/useradmin',methods=['GET', 'POST'])
def useradmin():
    form = SignOutForm()
    if form.validate_on_submit():
        return redirect(url_for("logoutadmin"))
    return render_template('Admin.html', form=form)

@app.route('/logout')
def logout():
    session.pop("uservol", None)
    return redirect(url_for("home"))

@app.route('/logoutorganization')
def logoutorganization():
    session.pop("userorg", None)
    return redirect(url_for("home"))

@app.route('/logoutadmin')
def logoutadmin():
    session.pop("useradm", None)
    return redirect(url_for("home"))


@app.route('/deleteVolunteer', methods=['GET', 'POST'])
def deleteVolunteer():
    form = DeleteVolunteerForm()

    if form.validate_on_submit():

        req = request.form
        usernameVolunteer = req["username"]

        Database()
        global cursor

        cursor.execute("SELECT * FROM `volunteer` WHERE `username` = ?",
                       (usernameVolunteer,))
        # if form.validate_on_submit():
        if cursor.fetchone() is not None:
            flash("Volunteer has been deleted")
        else:
            print("this Volunteer is not exits")
            return redirect(url_for('deleteVolunteer'))
        cursor.execute("DELETE FROM 'volunteer' WHERE username=?", (usernameVolunteer,))
        conn.commit()
        return render_template('deleteVolunteer.html', form=form, )

    return render_template('deleteVolunteer.html', form=form, )
@app.route('/deleteOrganization', methods=['GET', 'POST'])
def deleteOrganization():
    form = DeleteOrganizationForm()

    if form.validate_on_submit():

        req = request.form
        usernameOrganization = req["username"]

        Database()
        global cursor

        cursor.execute("SELECT * FROM `organization` WHERE `username` = ?",
                       (usernameOrganization,))
        # if form.validate_on_submit():
        if cursor.fetchone() is not None:
            flash("Organization has been deleted")
        else:
            print("this Organization is not exits")
            return redirect(url_for('deleteOrganization'))
        cursor.execute("DELETE FROM 'organization' WHERE username=?", (usernameOrganization,))
        conn.commit()
        return render_template('deleteOrganization.html', form=form, )

    return render_template('deleteOrganization.html', form=form, )

@app.route('/deleteField', methods=['GET', 'POST'])
def deleteField():
    form = DeleteFieldForm()

    if form.validate_on_submit():

        req = request.form
        nameField = req["field"]

        Database()
        global cursor

        cursor.execute("SELECT * FROM `organization` WHERE `hobby` = ?",
                       (nameField,))
        # if form.validate_on_submit():
        if cursor.fetchone() is not None:
            flash("this field has been deleted")
        else:
            print("this Field is not exits")
            return redirect(url_for('deleteField'))
        cursor.execute("DELETE FROM 'organization' WHERE hobby=?", (nameField,))
        conn.commit()
        return render_template('deleteField.html', form=form, )

    return render_template('deleteField.html', form=form, )

@app.route('/updateDonation', methods=['GET', 'POST'])
def updateDonation():
    form = UpdateDonationForm()

    if request.method == 'POST':
        donation = form.donation.data
        cursor.execute("UPDATE 'admin' SET donation=? WHERE username=?", (donation, 'admin'))
        conn.commit()
        cursor.close()
        conn.close()
    flash("successfully updated!")
    return render_template('updateDonation.html', form=form, )



if __name__ == '__main__':
    app.run(debug=True)