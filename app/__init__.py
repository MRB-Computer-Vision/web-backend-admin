# app/__init__.py
""" Global Setup to the API

"""
from flask_restx import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns
from .main.controllers.auth_controller import api as auth_ns
from .main.controllers.exam_controller import api_exams as exams_ns
from .main.controllers.exam_controller import api_exam as exam_ns
from .main.controllers.medical_record_controller import api_medical_record as medical_records_ns
blueprint = Blueprint('api', __name__)

authorizations = {
    'Basic Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(
    blueprint,
    title='FLASK REST API MRB WITH JWT',
    version='1.0',
    description='FLASK REST API WEBSERVICE',
    security='Bearer Auth',
    authorizations=authorizations
)

api.add_namespace(user_ns, path='/users')
api.add_namespace(exams_ns, path='/exams')
api.add_namespace(exam_ns, path='/exams')
api.add_namespace(medical_records_ns, path='/medical_records')
api.add_namespace(auth_ns)
