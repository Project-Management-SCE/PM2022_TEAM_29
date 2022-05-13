
#from App import Demand
from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField,SelectField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm
from wtforms import SelectField


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