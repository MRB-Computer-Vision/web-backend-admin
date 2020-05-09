# pylint: disable=no-member
# pylint: disable=missing-module-docstring
from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from .. import db, flask_bcrypt

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
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
        self.password = flask_bcrypt.generate_password_hash(password_without_hash).decode('utf-8')

    def check_password(self, password_without_hash):
        """ Method to check password if is correct
        """
        return flask_bcrypt.check_password_hash(self.password, password_without_hash)

    def __repr__(self):
        """ To string method
        """
        return "<User '{}'>".format(self.email)
        