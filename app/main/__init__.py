# pylint: disable=missing-module-docstring
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mail import Mail


from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
mail = Mail()

def create_app(config_name):
    """ Creatpp Flask App
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    mail.init_app(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    return app
