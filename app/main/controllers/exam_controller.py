# pylint: disable=missing-module-docstring
from flask import request
from flask_restx import Resource

from ..util.dto import ExamDto
from ..services.exam_service import add_exam, get_all_exams, get_an_exam, update_an_exam
from app.main.util.decorator import token_required

api = ExamDto.api
_exam = ExamDto.exam


@api.route('/')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class ExamList(Resource):
    """ ExamList Controller with get and post methods
    """
    @api.doc('list_of_registered_exams')
    @api.marshal_list_with(_exam, envelope='data')
    # @token_required
    def get(self):
        """List all registered exams"""
        return get_all_exams()

    @api.response(201, 'Exam successfully created.')
    @api.doc('create a new exams')
    @api.expect(_exam, validate=True)
    def post(self):
        """Creates a new Exam"""
        return add_exam(data=request.json)

@api.route('/<id>')
@api.param('id', 'The Exam identifier')
@api.response(404, 'User not found.')
class Exam(Resource):
    """ Exam Controller with get User by Id
    """
    @api.doc('get an Exame')
    @api.marshal_with(_exam)
    def get(self, _id):  # pylint: disable=redefined-builtin
        """get a user given its identifier"""
        exam = get_an_exam(_id)
        if not exam:
            api.abort(404)
        else:
            return exam

    @api.response(201, 'Exam Updated Successfully.')
    @api.doc('Update an Exame')
    def put(self, _id):
        """Update an Exame, specially on Result
        
        Get an json with the fields to update
        Note, use this route to change the exam result.
        """
        return update_an_exam(_id, data=request.json)
    
    


