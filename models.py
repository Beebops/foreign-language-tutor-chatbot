from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()


class User(UserMixin, db.Model):
    """User in the system"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    
    @classmethod
    def register(cls, username, email, password):
        """Registers a new user
        Hashes password and adds user to the system
        """

        hashed_password = bcrypt.generate_password_hash(password).decode("UTF-8")

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Find user when username and password is inputted.

        Class method that searches for a user whose password matches the entered password, and returns the user object if there is a match.
        If password is incorrect or a user isn't found, returns False
        """
        user = cls.query.filter_by(username=username).first()

        if user:
            is_authenticated = bcrypt.check_password_hash(user.password, password)
            if is_authenticated:
                return user

        return False    

def connect_db(app):
    """Connect this database to provided Flask app.

    Call this in your Flask app.
    """

    db.app = app
    db.init_app(app)