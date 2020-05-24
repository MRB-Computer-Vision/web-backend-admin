
from flask_restx import Resource
from flask import request

from app.main.util.decorator import token_required
from ..util.dto import EmailDTO
from ..services.email_service import send_email

api = EmailDTO.api

@api.route('/send_email')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class EmailForUser(Resource):
    """ Controller for send e-mail for a user
    """
    @api.doc('email for a user')
    @token_required
    def post(self):
        """List all registered exams"""
        data = request.get_json()
        return send_email(data["recipient"], data["body"])
