"""DTO classes

"""
from flask_restx import Namespace, fields


class UserDto:
    """ UserDTO Class
    """
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'id': fields.String(required=False, description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'is_admin': fields.Boolean(required=False, description='user check if is admin'),
        'is_active': fields.Boolean(required=False, description='user check if is active'),
    })


class AuthDto:
    """ Auth Class
    """
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class ExamDto:
    """ ExamDTO Class
    """
    api = Namespace('exams', description='exams related operations')
    exam = api.model('exams', {
        'id': fields.String(required=False, description='exam id'),
        'status': fields.String(required=True, description='status'),
        'created_at': fields.String(required=False, description='created_at'),
        'updated_at': fields.Boolean(required=False, description='updated_at'),
        'files': fields.Boolean(required=False, description='user check if is active')
    })

    child = api.inherit('Child', parent, {
        'extra': fields.String
    })