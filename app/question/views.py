from flask import render_template, request, jsonify
from ..models import Question, Answer
from .. import db
from flask import g
from . import question


@question.route('/sampletour')
def sample():
    question = Question.query.filter_by(question_id=1).first()
    answers = [i for i in Answer.query.filter_by(question_id=1).all()]
    return render_template('sample/sample.html', question=question, answers=answers)


@question.route('/sampletour/_answer')
def add_numbers():
    question_id = 1
    answer = request.args.get('answer', 0, type=int)
    correct_answer = Answer.query.filter_by(question_id=1).filter_by(correct=1).first()
    if correct_answer.answer_id == answer:
        answer_responce = jsonify(result=1)
        return answer_responce
    else:
        answer_responce = jsonify(result=0)
        return answer_responce