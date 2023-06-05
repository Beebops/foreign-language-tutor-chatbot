import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, login_manager
from flask_login import login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///foreign_language_tutor_db'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = True
app.config["SECRET_KEY"] = os.environ.get("LANGUAGE_TUTOR_SECRET_KEY")

toolbar = DebugToolbarExtension(app)
login_manager.init_app(app)

connect_db(app)
app.app_context().push()

# @app.route('/')
# def index():
#     user = User.query.filter_by(username).first()
#     login_user(user)
#     return 'You are now logged in'

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return "You are now logged out"

# @app.route('/home')
# @login_required
# def home():
#     return f"The current user is {current_user.username}"

if __name__ == "__main__":
    app.run(debug=True)