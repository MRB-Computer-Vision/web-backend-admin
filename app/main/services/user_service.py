# pylint: disable=missing-module-docstring
from app.main import db
from app.main.models.user import User


def save_new_user(data):
    """Save new User on database

        Parameters
        ----------
        data: dict
            Request JSON body

        Returns
        -------
        tuple: message, HTTP Response
            Return the JSON message and HTTP Response
    """
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            password_without_hash=data['password']
        )
        save_changes(new_user)

        return generate_token(new_user)
        # response_object = {
        #     'success': True,
        #     'message': 'Successfully registered.'
        # }
        # return response_object, 201
    else:
        response_object = {
            'success': False,
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    """ Return all users from database
    """
    return User.query.all()


def get_a_user(_id):  # pylint: disable=redefined-builtin
    """ Get User by ID
    """
    return User.query.filter_by(id=_id).first()


def save_changes(data):
    """ Save changes on database
    """
    db.session.add(data)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'success': True,
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'success': False,
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
