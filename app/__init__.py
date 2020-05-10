# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns
from .main.controllers.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK REST API MRB WITH JWT',
          version='1.0',
          description='FLASK REST API WEBSERVICE'
          )

api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns)
