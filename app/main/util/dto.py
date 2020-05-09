from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'id': fields.String(required=False, description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'is_admin': fields.Boolean(required=False, description='user check if is admin'),
        'is_active': fields.Boolean(required=False, description='user check if is active'),
    })
    