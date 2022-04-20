
#from App import Demand
from flask import  Flask,render_template,session,redirect,url_for
from wtforms import StringField, PasswordField , SubmitField , RadioField,TextAreaField,SelectField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired,Length,EqualTo, Email
from flask_wtf import FlaskForm


