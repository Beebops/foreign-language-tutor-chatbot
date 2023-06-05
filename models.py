from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

class Chat(db.Model):
    """Model of a user's chat"""

    __tablename__ = "chats"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        ondelete="cascade")
    
    language = db.Column(db.String(75), nullable=False)

    language_level = db.Column(db.String(15), nullable=False)

class Chat_log(db.Model):
    """Model of messages produced by either the user or assistant in a chat"""

    __tablename__ = "chat_logs"

    id = db.Column(db.Integer, primary_key=True)

    role = db.Column(db.String(50), nullable=False)

    content = db.Column(db.Text)

    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow())
    
    chat_id = db.Column(
        db.Integer,
        db.ForeignKey("chats.id"),
        ondelete="cascade")
    

class User(UserMixin, db.Model):
    """User in the system"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(120), nullable=False, unique=True)

    email = db.Column(db.String(120), nullable=False, unique=True)

    password = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"<User #{self.id}: {self.username}>"
    
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

@login_manager.user_loader
def load_user(user_id):
    """ Returns the user instance with the passed in user id"""

    return User.query.get(int(user_id))

def connect_db(app):
    """Connect database to provided Flask app.

    Call this in your Flask app.
    """

    db.app = app
    db.init_app(app)