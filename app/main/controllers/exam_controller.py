# pylint: disable=missing-module-docstring
from flask import request
from flask_restx import Resource

from ..util.dto import ExamDto
from ..services.exam_service import add_exam, get_all_exams, get_an_exam, update_an_exam
from app.main.util.decorator import token_required
from app.main.services.auth_service import Auth
api_exams = ExamDto.api
_exams = ExamDto.exam


@api_exams.route('/')
@api_exams.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class ExamList(Resource):
    """ ExamList Controller with get and post methods
    """
    @api_exams.doc('list_of_registered_exams')
    @api_exams.marshal_list_with(_exams, envelope='data')
    @token_required
    def get(self):
        """List all registered exams"""
        return get_all_exams()

    @api_exams.response(201, 'Exam successfully created.')
    @api_exams.doc('create a new exams')
    @api_exams.expect(_exams, validate=True)
    @token_required
    def post(self):
        """Creates a new Exam"""
        current_user = Auth.get_logged_in_user(request)[0]['data']
        return add_exam(data=request.json, current_user=current_user)


api_exam = ExamDto.api
_exam = ExamDto.exam


@api_exam.route('/<_id>')
@api_exam.param('id', 'The Exam identifier')
@api_exam.response(404, 'Exam not found.')
class Exam(Resource):
    """ Exam Controller with get User by Id
    """
    @api_exam.doc('get an Exame')
    @api_exam.marshal_with(_exam)
    def get(self, _id):  # pylint: disable=redefined-builtin
        """get a user given its identifier"""
        exam = get_an_exam(_id)
        if not exam:
            api.abort(404)
        else:
            return exam

    @api_exam.response(202, 'Exam updated sucessfully.')
    @api_exam.doc('Update an Exame')
    @api_exam.expect(_exam, validate=True)
    def put(self, _id):
        """Update an Exame, specially on Result

        Get an json with the fields to update
        Note, use this route to change the exam result.
        """

        return update_an_exam(_id, data=request.json)
