# pylint: disable=no-member

from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .. import db
import enum


class StatusEnum(enum.Enum):
    pedding = 'pedding'
    processing = 'processing'
    processed = 'processed'
    error = 'error'


class Exam(db.Model):
    """
    Exame Model for storing JWT tokens
    """
    __tablename__ = 'exames'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4, unique=True, nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default="pending")
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __init__(self):
        pass

    def __repr__(self):
        return '<id: token: {}'.format(self.token)


class ExamFile(db.Model):
    """
    Exame Model for storing JWT tokens
    """
    __tablename__ = 'exam_files'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4, unique=True, nullable=False)

    exam_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("Exam.id"))
    order = db.Column(db.Integer)
    exam = relationship("Exam", back_populates="exam_files", single_parent=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)
