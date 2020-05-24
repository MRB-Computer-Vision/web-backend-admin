# pylint: disable=missing-module-docstring
from app.main import db
from app.main.models.exam import Exam, ExamFile
from app.main.repositories.exam_repository import ExamRepository
import json

def add_exam(data):
    # pylint: disable=no-member

    try:
        exam_repository = ExamRepository()
        exam = exam_repository.save(data)
        response_object = {
            'success': True,
            'message': 'Exam added successfully.'
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


def get_an_exam(_id):  # pylint: disable=redefined-builtin
    """ Get User by ID
    """
    return Exam.query.filter_by(id=_id).first()

def update_an_exam(_id, data):
    """"""
    try:
        exam_repository = ExamRepository()
        exam_repository.update(data)
        response_object = {
            'success': True,
            'message': 'Exam Updated successfully.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'success': False,
            'message': e
        }
        return response_object, 400

def delete_an_exam(_id):
    pass
