from flask import Flask, render_template, request, flash, session, redirect, url_for, abort
import sqlite3
from forms import signupForm, SignOutForm, LoginForm, signupFormOrg, DeleteVolunteerForm, DeleteOrganizationForm, DeleteFieldForm, UpdateDonationForm, DivideDonationForm, UpdateRatingForm, AddFieldForm, SearchForVolunteerForm
from datetime import datetime
from werkzeug.utils import secure_filename
from PIL import Image
import PIL
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

def Database():
    global conn, cursor
    conn = sqlite3.connect("Giving__DB.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (username TEXT PRIMARY KEY NOT NULL, password TEXT, donation TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `organization` (username TEXT PRIMARY KEY NOT NULL, password TEXT, age INTEGER, location TEXT, phone TEXT, name TEXT, maxvol TEXT, rating TEXT, numvol TEXT, donation TEXT, hobby TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `volunteer` (username TEXT PRIMARY KEY NOT NULL, password TEXT, age INTEGER, location TEXT, phone TEXT, name TEXT, hour INTEGER, hobby TEXT, meen TEXT, pic TEXT, perm TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `hours` (orgname TEXT NOT NULL,volname TEXT NOT NULL, hour INTEGER, limitt TEXT , PRIMARY KEY(orgname,volname)) ")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `apply` (orgname TEXT NOT NULL,volname TEXT NOT NULL, age INTEGER, location TEXT, phone TEXT, email TEXT, meen TEXT, hobby TEXT, id TEXT, job TEXT, PRIMARY KEY(orgname,volname)) ")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `report` (orgg TEXT NOT NULL,voll TEXT NOT NULL, hour INTEGER, status TEXT NOT NULL,datte TEXT ,PRIMARY KEY(orgg,voll,datte)) ")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `Fields` (name TEXT PRIMARY KEY NOT NULL, f TEXT) ")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `Search` (org TEXT PRIMARY KEY NOT NULL, meen TEXT, geel TEXT, mekom TEXT, hoby TEXT) ")

import urllib.request

Database()
app.config['SECRET_KEY'] = 'Sujood'

import json
import os
import tempfile
from werkzeug.utils import secure_filename
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

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
        session["uservol"] = form.username.data
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
    return render_template('register.html', form=form)

# Add new volunteer 
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
    guest = cursor.execute("SELECT * FROM `Fields`")
    form.hobby.choices = [(x[0]) for x in guest]
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
    return render_template('registerOrg.html', form=form)
#this to insert an organization
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
        cursor.execute("UPDATE 'admin' SET donation=? WHERE username=?", (donation, session["useradm"],))
        conn.commit()
    return render_template('updateDonation.html', form=form, )

@app.route('/divideDonation', methods=['GET', 'POST']) #donation value
def divideDonation():
    session["useradm"] = "admin"
    guest = cursor.execute("SELECT donation FROM `admin` WHERE `username` = ?", (session["useradm"],))
    str1 = ''
    users=[]
    for x in guest:
        str1 = str1.join(x)
        users.append(str1)
    form = DivideDonationForm()


    if request.method == 'POST':
        donation = form.donation.data
        username = form.username.data
        cursor.execute("UPDATE 'organization' SET donation=? WHERE username=?", (donation, username,))
        conn.commit()
        aa = int(str1)-int(donation)
        s = str(aa)
        cursor.execute("UPDATE 'admin' SET donation=? WHERE username=?", (aa, session["useradm"],))
        conn.commit()
    return render_template('divideDonation.html', form=form, guest=users)

@app.route('/updateRating', methods=['POST','GET'])
def updateRating():
    Database()
    form = UpdateRatingForm()
    if request.method == 'POST':
        rating = form.rating.data
        username = form.username.data
        cursor.execute("UPDATE 'organization' SET rating=? WHERE username=?", (rating, username,))
        conn.commit()
    return render_template('updateRating.html', form=form, )

# @app.route('/addField', methods=['GET', 'POST'])
# def addField():
#     #form = AddFieldForm()
#
#     if request.method == 'POST':
#         field = form.field.data
#         cursor.execute("UPDATE 'organization' SET hobby=? WHERE username=?", (field, "ssss",))
#         conn.commit()
#     return render_template('addField.html', form=form, )

def delete(usename):
    Database()
    global cursor
    cursor.execute("DELETE FROM 'volunteer' WHERE username=?", (usename,))
    conn.commit()

def delete_org(usename):
    Database()
    global cursor
    cursor.execute("DELETE FROM 'volunteer' WHERE username=?", (usename,))
    conn.commit()

#delete field of volunteering
def delete_field(f):
    Database()
    global cursor
    cursor.execute("DELETE FROM 'organization' WHERE hobby=?", (f,))
    conn.commit()

def update_donation(donation):
    Database()
    global cursor
    cursor.execute("UPDATE 'admin' SET donation=? WHERE username=?", (donation, session["useradm"],))
    conn.commit()

def divide_donation(donation, username):
    Database()
    global cursor
    cursor.execute("UPDATE 'organization' SET donation=? WHERE username=?", (donation, username,))
    conn.commit()
#Add new field of volunteering  
def add_field(field):
    Database()
    global cursor
    cursor.execute("UPDATE 'organization' SET hobby=? WHERE username=?", (field, "ssss",))
    conn.commit()

def update_rating(rating,username):
    Database()
    global cursor
    cursor.execute("UPDATE 'organization' SET name=? WHERE username=?", (rating, username,))
    conn.commit()


@app.route('/addFieldAdmin', methods=['GET', 'POST'])
def addFieldAdmin():
    Database()
    form = AddFieldForm()

    if request.method == 'POST':
        field = form.field.data
        cursor.execute(
            "INSERT INTO `Fields` (name,f) VALUES(?,?)", (field,"ok"))
        conn.commit()
    return render_template('addField.html', form=form, )

def add_Field_Admin(field):
    Database()
    global cursor
    cursor.execute(
        "INSERT INTO `Fields` (name,f) VALUES(?,?)", (field, "ok"))
    conn.commit()

@app.route("/upload",methods=['GET','POST'])
def upload():

    Database()
    global cursor
    file_path = 'images/'
    file_name = "sys"
    full_path = file_path + file_name + '.jpg'
    url = "https://abroadship.org/wp-content/uploads/2018/11/volunteer-wordall.png"
    urllib.request.urlretrieve(url, full_path)
    cursor.execute("UPDATE 'volunteer' SET pic=? WHERE username=?", (url, session["uservol"],))
    conn.commit()

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)


                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("upload.html")

@app.route("/uploadFile",methods=['GET','POST'])
def uploadFile():

    Database()
    global cursor
    file_path = 'images/'
    file_name = "sys"
    full_path = file_path + file_name + '.jpg'
    url = "https://abroadship.org/wp-content/uploads/2018/11/volunteer-wordall.png"
    urllib.request.urlretrieve(url, full_path)
    cursor.execute("UPDATE 'volunteer' SET perm=? WHERE username=?", (url, session["uservol"],))
    conn.commit()

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image1"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)


                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("upload.html")

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route('/SearchForVolunteer', methods=['GET', 'POST'])
def SearchForVolunteer():
    form = SearchForVolunteerForm()
    Database()
    cursor.execute("DELETE FROM 'Search' WHERE org=?", (session["userorg"],))
    conn.commit()
    if request.method == 'POST':
        meen = form.meen.data
        geel = form.geel.data
        mekom = form.mekom.data
        hoby = form.hoby.data
        cursor.execute(
        "INSERT INTO `Search` (org, meen, geel, mekom, hoby) VALUES(?,?, ?, ?,?)",
        (session["userorg"], meen, geel, mekom, hoby))
        conn.commit()

    return render_template('SearchForVolunteer.html', form=form)

@app.route('/Show', methods=['GET', 'POST'])
def Show():
    Database()
    guests=()
    x = cursor.execute("SELECT * FROM `Search` WHERE `org` = ?", (session["userorg"],))
    # for y in x:
    y=cursor.fetchall()[0]
    mn = y[1]
    g = y[2]
    mm = y[3]
    h = y[4]
    if(mn==None):
        mn=''
    if (g == None):
        g = ''
    if (mm == None):
        mm = ''
    if (h == None):
        h = ''
    if((mn !='' )& (g !='') & (mm !='') & (h !='')):
        guests = cursor.execute("SELECT * FROM `volunteer` WHERE `meen` = ? AND `age` = ? AND `location` = ? AND `hobby` = ?", (mn,int(g),mm,h,))
    if ((mn !='')& (g !='') & (mm !='' )):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `age` = ? AND `location` = ?",
            (mn, int(g), mm,))
    if ((mn !='') & (g !='') & (h !='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `age` = ? AND `hobby` = ?",
            (mn, int(g), h,))
    if ((mn !='') & (mm !='') & (h !='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `location` = ? AND `hobby` = ?",
            (mn, mm, h,))

    if ( (g!='') & (mm!='' )& (h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `age` = ? AND `location` = ? AND `hobby` = ?",
            ( int(g), mm, h,))
    if ((mn!='') & (g!='') ):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `age` = ? ",
            (mn, int(g),))
    if ((mn!='') & (mm!='') ):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ?  AND `location` = ?",
            (mn, mm,))
    if ( (g!='') & (mm!='') ):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE  `age` = ? AND `location` = ?",
            ( int(g), mm,))
    if ((mn!='') & (g!='') ):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `age` = ? ",
            (mn, int(g),))
    if ((mn!='') &(h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `hobby` = ?",
            (mn, h,))
    if ( (g!='' )& (h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE  `age` = ? AND `hobby` = ?",
            ( int(g), h,))
    if ((mn!='') &( mm!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `location` = ? ",
            (mn, mm,))
    if ((mn!='') &( h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `meen` = ? AND `hobby` = ?",
            (mn, h,))
    if ( (mm !='')& (h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `location` = ? AND `hobby` = ?",
            ( mm, h,))
    if ( (g !='')&( mm!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `age` = ? AND `location` = ? ",
            ( int(g), mm,))
    if (( g!='') & (h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `age` = ? AND `hobby` = ?",
            ( int(g), h,))
    if ( (mm!='') & (h!='')):
        guests = cursor.execute(
            "SELECT * FROM `volunteer` WHERE `location` = ? AND `hobby` = ?",
            (mm, h,))
    if (g!=''):
        guests = cursor.execute("SELECT * FROM `volunteer` WHERE `age` = ?", (int(g),))
    if (mm!=''):
        guests = cursor.execute("SELECT * FROM `volunteer` WHERE `location` = ?", (mm,))
    if (h!=''):
        guests = cursor.execute("SELECT * FROM `volunteer` WHERE `hobby` = ?", (h,))

    return render_template('Show.html', guests=guests)


def Search_Somone(username,mn, g, mm, h):
    Database()
    global cursor
    cursor.execute(
        "INSERT INTO `Search` (org, meen, geel, mekom, hoby) VALUES(?,?, ?, ?,?)",
        (username, mn, g, mm, h))
    conn.commit()

    
if __name__ == '__main__':
    app.run(debug=True)