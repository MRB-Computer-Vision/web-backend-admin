# pylint: disable=no-member
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .. import db
from ..models.exam import Exam, ExamFile
from ..models.user import User

class MedicalRecord(db.Model):
    """
    Exame Model for storing JWT tokens
    """
    __tablename__ = 'medical_records'

    id = db.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid4, unique=True, nullable=False)
    user = relationship(
        "User", back_populates="medical_records", single_parent=True)
    user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("users.id"))
    number = db.Column(db.String(255), nullable=False)
    exams = relationship("Exam", back_populates="exam")

    def __init__(self):
        pass

    def to_json(self):
        return {
            'id': str(self.id),
            'number': self.number,
            'exams': [exam.to_json() for exam in self.exams]
        }
