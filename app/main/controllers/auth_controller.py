""" Auth Controller
"""
from flask import request
from flask_restx import Resource

from app.main.services.auth_service import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        """ Post Login
        """
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        """ Post Logout
        """
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
