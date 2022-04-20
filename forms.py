
#from App import Demand
from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField,SelectField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm


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
