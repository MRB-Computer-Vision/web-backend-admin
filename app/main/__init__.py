# pylint: disable=missing-module-docstring
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    """ Creatpp Flask App
    """
    app = Flask(__name__)
    #FIXME: It should load the config_name, but it is broken!
    app.config.from_object(config_by_name['dev'])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    return app
