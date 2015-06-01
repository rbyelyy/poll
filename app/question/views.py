from datetime import datetime
from flask import render_template, redirect, request, url_for, flash, jsonify
from flask.ext.login import login_user, logout_user, login_required, current_user
from .. import auth
from ..models import Question, Answer
from .. import db
from flask import g
from . import question


@question.route('/sampletour')
def sample():
    question = Question.query.filter_by(question_id=1).first()
    answers = [i for i in Answer.query.filter_by(question_id=1).all()]
    newvariable  =3
    return render_template('sample/sample.html', question=question, answers=answers, newvariable=newvariable)

@question.route('/sampletour/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    print request.args
    return jsonify(result=a + b)