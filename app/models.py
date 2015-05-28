__author__ = 'rbs'
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


class Users(UserMixin, db.Model):
    __tablename__     = 'users'
    password_hash     = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    user_id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    confirmed = db.Column(db.Boolean, unique=False, default=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow,  nullable=False)
    last_login_date = db.Column(db.DateTime, nullable=True)
    confirmed_date = db.Column(db.DateTime, nullable=True)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class History(db.Model):
    __tablename__ = 'history'

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    poll_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.String(64), db.ForeignKey('users.user_id'), nullable=True)
    user_id = db.Column(db.String(64), db.ForeignKey('questions.question_id'), nullable=True)
    correct_answer_id = db.Column(db.String(64), db.ForeignKey('answers.answer_id'), nullable=True)
    user_answer_id = db.Column(db.String(64), db.ForeignKey('answers.answer_id'), nullable=True)


class Questions(db.Model):
    __tablename__ = 'questions'

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    question_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    question = db.Column(db.Text(), nullable=True)
    image_path = db.Column(db.String(128), db.ForeignKey('users.user_id'), nullable=True)
    confirmed = db.Column(db.Boolean, nullable=False)


class Answers(db.Model):
    __tablename__        = 'answers'

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    question_id          = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    answer_id            = db.Column(db.Integer, primary_key=True, unique=False, nullable=False)
    answer_text          = db.Column(db.Text(), nullable=True)
    correct              = db.Column(db.Boolean, nullable=True)