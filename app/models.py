from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager
from flask import current_app


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class History(db.Model):
    __tablename__ = 'history'

    poll_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.String(64), db.ForeignKey('questions.question_id'), nullable=True)
    user_id = db.Column(db.String(64), db.ForeignKey('users.id'), nullable=True)
    correct_answer_id = db.Column(db.String(64), db.ForeignKey('answers.answer_id'), nullable=True)
    user_answer_id = db.Column(db.String(64), db.ForeignKey('answers.answer_id'), nullable=True)
    users = db.relationship('User')


class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    question = db.Column(db.Text(), nullable=True)
    image_path = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, nullable=False)
    answer = db.relationship("Answer", backref="questions")


class Answer(db.Model):
    __tablename__ = 'answers'

    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
    answer_id = db.Column(db.Integer, primary_key=True, unique=False, nullable=False)
    answer_text = db.Column(db.Text(), nullable=True)
    correct = db.Column(db.Boolean, nullable=True)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, unique=False, default=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow,  nullable=False)
    last_login_date = db.Column(db.DateTime, nullable=True)
    confirmed_date = db.Column(db.DateTime, nullable=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))