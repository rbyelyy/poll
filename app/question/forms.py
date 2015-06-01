from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError


class QuestionForm(Form):
    question = StringField('Question', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Next')