# pylint: disable=no-member
# pylint: disable=missing-module-docstring
# pylint: disable=broad-except
from datetime import datetime, timedelta
from uuid import uuid4
import jwt
from sqlalchemy.dialects.postgresql import UUID
from app.main.models.blacklist import BlacklistToken
from .. import db, flask_bcrypt
from ..config import key


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4, unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    @property
    def password_without_hash(self):
        """ Method to create an temporary password withou hash
        """
        raise AttributeError('password_without_hash: write-only field')

    @password_without_hash.setter
    def password_without_hash(self, password_without_hash):
        """ Method to create the hash and set on password attribute
        """
        self.password = flask_bcrypt.generate_password_hash(
            password_without_hash).decode('utf-8')

    def check_password(self, password_without_hash):
        """ Method to check password if is correct
        """
        return flask_bcrypt.check_password_hash(self.password, password_without_hash)

    def __repr__(self):
        """ To string method
        """
        return "<User '{}'>".format(self.email)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1, seconds=5),
                'iat': datetime.utcnow(),
                'sub': str(user_id)
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as _e:
            return _e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
