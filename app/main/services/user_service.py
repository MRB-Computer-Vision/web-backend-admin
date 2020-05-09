import uuid
import datetime

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
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()