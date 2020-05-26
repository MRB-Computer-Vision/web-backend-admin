# pylint: disable=missing-module-docstring
from app.main import db
from app.main.models.exam import Exam, ExamFile
from app.main.repositories.exam_repository import ExamRepository
from covid_vision.ml.models.covid_cxr import CovidCXR
import os
import boto3
from urllib.parse import unquote

def add_exam(data):
    # pylint: disable=no-member

    try:
        exam_repository = ExamRepository()
        exam = exam_repository.save(data)
        # run prediction
        result = run_covid_predict(exam)
        exam_repository.update_exam_result(result)
        response_object = {
            'success': True,
            'message': 'Exam added with successfully.',
            'data': exam.to_json()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'success': False,
            'message': e
        }
        return response_object, 200

def get_all_exams():
    """ Return all exams from database
    """
    return Exam.query.all()


def get_a_exam(_id):  # pylint: disable=redefined-builtin
    """ Get User by ID
    """
    return Exam.query.filter_by(id=_id).first()

def run_covid_predict(exam):
    file_path = os.path.abspath(os.getcwd()) + '/app/main/tmp/'
    if not os.path.exists(file_path): os.makedirs(file_path)
    clf = CovidCXR()
    s3 = boto3.client('s3', aws_access_key_id = os.getenv('S3_ACCESS_KEY'), aws_secret_access_key = os.getenv('S3_ACCESS_SECRET'))
    # TODO improve the prediction result loop
    for exam_file in exam.exam_files:
        file_name = unquote(exam_file.file_path.partition('.com/')[-1])
        s3.download_file(os.getenv('S3_BUCKET_NAME'), file_name, file_path + 'test.png')
        img = clf.read_image(file_path + 'test.png')
        result = clf.predict(img)
        prediction = clf.CLASSES[result.argmax()]
    return prediction