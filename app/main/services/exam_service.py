# pylint: disable=missing-module-docstring
from app.main import db
from app.main.models.exam import Exam, ExamFile


def add_exam(exam_params):
    # pylint: disable=no-member
    exam = Exam()
    try:
        # insert the token
        db.session.add(exam)
        db.session.commit()
        response_object = {
            'success': True,
            'message': 'Exam added with successfully.'
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'success': False,
            'message': e
        }
        return response_object, 200


def get_all_exams():
    """ Return all exams from database
    """
    return Exam.query.all()


def get_a_exam(_id):  # pylint: disable=redefined-builtin
    """ Get User by ID
    """
    return Exam.query.filter_by(id=_id).first()
