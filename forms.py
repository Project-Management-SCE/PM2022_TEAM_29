
#from App import Demand
from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField,SelectField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields import DateField
from wtforms import DateField


class signupForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=5, max=8)])
    name = StringField(label='name', validators=[DataRequired(), Length(min=3, max=50)])
    age = StringField(label='age', validators=[DataRequired(), Length(min=1, max=20)])
    location = StringField(label='location', validators=[DataRequired(), Length(min=3, max=50)])
    phone = StringField(label='phone', validators=[DataRequired(), Length(min=3, max=20)])
    hour = StringField(label='hour', validators=[DataRequired(), Length(min=3, max=20)])
    hobby = StringField(label='hobby', validators=[DataRequired(), Length(min=3, max=50)])
    submit = SubmitField(label='Sign up')

class SignOutForm(FlaskForm):
    submit = SubmitField('logout')

class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Log in')


class signupFormOrg(FlaskForm):
    username = StringField(label='username', validators=[DataRequired(), Length(min=4, max=30)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=5, max=8)])
    age = StringField(label='age limit', validators=[DataRequired(), Length(min=1, max=20)])
    location = StringField(label='location', validators=[DataRequired(), Length(min=3, max=50)])
    phone = StringField(label='phone', validators=[DataRequired(), Length(min=3, max=20)])
    name = StringField(label='name of the organization', validators=[DataRequired(), Length(min=3, max=50)])
    maxvol = StringField(label='maximum number of volunteers', validators=[DataRequired(), Length(min=1, max=50)])
    hobby = SelectField('the organization volunteering field', choices=[])
    submit = SubmitField(label='Sign up')

class DeleteVolunteerForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    submit = SubmitField('Delete Volunteer')

class DeleteOrganizationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    submit = SubmitField('Delete Organization')

class DeleteFieldForm(FlaskForm):
    field = StringField("filed", validators=[DataRequired()])
    submit = SubmitField('Delete Field')

class UpdateDonationForm(FlaskForm):
    donation = StringField("donation", validators=[DataRequired()])
    submit = SubmitField('update donation')

class DivideDonationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    donation = StringField("donation", validators=[DataRequired()])
    submit = SubmitField('give donation')

class UpdateRatingForm(FlaskForm):
    username = StringField("organization_name", validators=[DataRequired()])
    rating = StringField("rating", validators=[DataRequired()])
    submit = SubmitField('update rating')

class AddFieldForm(FlaskForm):
    field = StringField("field", validators=[DataRequired()])
    submit = SubmitField('add field')

class SearchForVolunteerForm(FlaskForm):
    meen = StringField("gender:")
    geel = StringField("age:")
    mekom = StringField("location:")
    hoby = StringField("work filed:")
    submit = SubmitField('check')

class ReportHoursForm(FlaskForm):
    ddate = DateField('calender:', format='%Y-%M-%D', validators=(validators.DataRequired(),))
    ddaate = StringField("date:(in format D-M-Y )", validators=[DataRequired()])
    hhour = StringField("number of hours:", validators=[DataRequired()])
    organ = StringField("organization name:", validators=[DataRequired()])
    data = StringField("tell us more:", validators=[DataRequired()])
    submit = SubmitField('add report')

class UpdateMaxVolForm(FlaskForm):
    maxvol = StringField("New Max number", validators=[DataRequired()])
    submit = SubmitField('update number')

class UpdateMaxHourForm(FlaskForm):
    username = StringField("volunteer name", validators=[DataRequired()])
    Maxhour = StringField("new hours number", validators=[DataRequired()])
    submit = SubmitField('update Max Hour')

class ApplyForOrgForm(FlaskForm):
    name = StringField(label='first name', validators=[DataRequired(), Length(min=4, max=30)])
    age = StringField(label='age:', validators=[DataRequired(), Length(min=1, max=20)])
    location = StringField(label='location', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField(label='email', validators=[DataRequired(), Length(min=3, max=50)])
    phone = StringField(label='phone', validators=[DataRequired(), Length(min=3, max=20)])
    meen = SelectField('the organization volunteering field', choices=['male', 'female'])
    id = StringField(label='identity number', validators=[DataRequired(), Length(min=1, max=50)])
    hobby = StringField(label='hobby:', validators=[DataRequired(), Length(min=1, max=50)])
    job = StringField('what is your job?', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField(label='Apply')



