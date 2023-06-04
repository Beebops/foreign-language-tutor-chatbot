import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, login_manager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///foreign_language_tutor_db'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = True
app.config['SECRET_KEY'] = os.environ.get('LANGUAGE_TUTOR_SECRET_KEY')

toolbar = DebugToolbarExtension(app)
login_manager.init_app(app)

connect_db(app)
app.app_context().push()