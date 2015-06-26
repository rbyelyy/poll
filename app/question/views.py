from flask import render_template, request, jsonify, make_response
from ..models import Question, Answer
from .. import db
from flask import g
from . import question

def question_selection(question_id=None):
    # TODO: Add validation for argument formats
    if question_id:
        return str((question_id))
    else:
        return '1'


@question.route('/sampletour')
def show_question():
    # TODO: Add expiration to cookies
    # TODO: Get limit of questions
    question_id = question_selection(request.cookies.get('question_id'))
    print type(question_id)
    if not 1 < int(question_id) < 4:
        question_id = '1'
    question = Question.query.filter_by(question_id=question_id).first()
    answers = [i for i in Answer.query.filter_by(question_id=question_id).all()]
    resp = make_response(render_template('sample/sample.html',
                                         question=question,
                                         answers=answers,
                                         question_id=question_id))
    resp.set_cookie('question_id', question_id)
    return resp


@question.route('/sampletour/_answer')
def _check_answer():
    question_id = question_selection(request.cookies.get('question_id'))
    answer = request.args.get('answer', 0, type=int)
    correct_answer = Answer.query.filter_by(question_id=question_id).filter_by(correct=1).first()
    if correct_answer.answer_id == answer:
        answer_responce = jsonify(result=1)
        return answer_responce
    else:
        answer_responce = jsonify(result=0)
        return answer_responce

@question.route('/sampletour/_quize')
def _check_quize():
    return render_template('sample/result.html')
