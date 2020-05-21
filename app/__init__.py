# app/__init__.py
""" Global Setup to the API

"""
from flask_restx import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns
from .main.controllers.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

# authorizations = {
#     'Basic Auth': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization',
#         'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**,
#  where JWT is the token"
#     }
# }

api = Api(blueprint,
          title='FLASK REST API MRB WITH JWT',
          version='1.0',
          description='FLASK REST API WEBSERVICE',
          security='Bearer Auth',
          #   authorizations=authorizations
          )

api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns)
