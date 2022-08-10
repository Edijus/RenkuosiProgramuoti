from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[validators.DataRequired(), validators.EqualTo('password2', message ='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Sign up')


class SignInForm(FlaskForm):
    email_address = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

