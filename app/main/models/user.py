from uuid import uuid4
from datetime import datetime
from .. import db, flask_bcrypt
from sqlalchemy.dialects.postgresql import UUID

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
        raise AttributeError('password_without_hash: write-only field')

    @password_without_hash.setter
    def password_without_hash(self, password_without_hash):
        self.password = flask_bcrypt.generate_password_hash(password_without_hash).decode('utf-8')

    def check_password(self, password_without_hash):
        return flask_bcrypt.check_password_hash(self.password, password_without_hash)

    def __repr__(self):
        return "<User '{}'>".format(self.email)