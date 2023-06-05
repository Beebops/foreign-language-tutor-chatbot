from wtforms import StringField, PasswordField, ValidationError, EqualTo, validators
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email
import email_validator
from flask_login import current_user
from models import User

class login_form(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=72)])

class registration_form(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=72)])
    password_copy = PasswordField("Re-enter Password", validators=[InputRequired(), Length(min=8, max=72), EqualTo("password", message="Passwords must match!")])

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email already registered!")

    def validate_usrname(self, usrname):
        if User.query.filter_by(username=usrname.data).first():
            raise ValidationError("Username already taken!")    



