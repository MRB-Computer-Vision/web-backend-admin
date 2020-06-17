# pylint: disable=missing-module-docstring
from flask import request
from flask_restx import Resource

from ..util.dto import MedicalRecordDto
from app.main.util.decorator import token_required
from ..services.medical_record_service import get_user_medical_records

api_medical_record = MedicalRecordDto.api
_medical_record = MedicalRecordDto.medical_record


@api_medical_record.route('/')
@api_medical_record.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class ExamList(Resource):
    """ ExamList Controller with get and post methods
    """
    @api_medical_record.doc('list_of_registered_medical_record')
    @api_medical_record.marshal_list_with(_medical_record, envelope='data')
    # @token_required
    def get(self):
        """List all registered exams"""
        #get current user id from session
        current_user_id = ''
        medical_records = get_user_medical_records(current_user_id)
        if not medical_records:
            api_medical_record.abort(404)
        else:
            return medical_records
