from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email


class SignUpForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=4,max=30)])
    email=StringField("Email",validators=[DataRequired(),Length(max=80)])
    password=PasswordField("Password",validators=[DataRequired(),Length(max=20),EqualTo('confirm')])
    comm_type=StringField("Commodities to sell ",validators=[DataRequired()])
    confirm=PasswordField("Confirm Password",validators=[DataRequired(),Length(max=20)])
    submit=SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Length(max=80)])
    password=PasswordField("Password",validators=[DataRequired(),Length(max=20),EqualTo('confirm')])
    submit=SubmitField("Log In")