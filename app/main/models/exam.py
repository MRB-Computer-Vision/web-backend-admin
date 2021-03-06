# pylint: disable=no-member

from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .. import db
import enum
import json


class StatusEnum(enum.Enum):
    pending = 'pending'
    processing = 'processing'
    processed = 'processed'
    error = 'error'


class Exam(db.Model):
    """
    Exame Model for storing JWT tokens
    """
    __tablename__ = 'exams'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4, unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    exam_files = relationship("ExamFile", back_populates="exam")
    percentage = db.Column(db.Float)
    result = db.Column(db.String(255), nullable=True)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default="pending")
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __init__(self):
        pass

    def to_json(self, rel=None):
        def extended_encoder(x):
            if isinstance(x, datetime):
                return x.isoformat()
            if isinstance(x, UUID):
                return str(x)
        return json.dumps(self.to_dict(), default=extended_encoder)

    # def __repr__(self):
    #     return '<id: token: {}'.format(self.token)

    def to_json(self):
        return {
            'id': str(self.id),
            'type': self.type,
            'result': self.result,
            'status': self.status.name,
            'exam_files': [exam_file.to_json() for exam_file in self.exam_files]
        }


class ExamFile(db.Model):
    """
    Exame Model for storing JWT tokens
    """
    __tablename__ = 'exam_files'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4, unique=True, nullable=False)

    exam_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("exams.id"))
    #order = db.Column(db.Integer)
    exam = relationship(
        "Exam", back_populates="exam_files", single_parent=True)
    file_path = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __init__(self, file_path):
        self.file_path = file_path
        #self.token = token
        #self.blacklisted_on = datetime.now()

    def to_json(self):
        return {
            'id': str(self.id),
            'file_path': self.file_path
        }

    # def __repr__(self):
    #     return '<id: token: {}'.format(self.token)
