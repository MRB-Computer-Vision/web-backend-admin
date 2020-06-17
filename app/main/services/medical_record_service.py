# pylint: disable=missing-module-docstring
from app.main.models.medical_record import MedicalRecord


def get_user_medical_records(user_id):
    return MedicalRecord.query.filter_by(user_id=user_id).all()
