import os
import unittest

from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app.main.models import user
from app.main.models import blacklist
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

try:
    from flask.cli import load_dotenv
    from pathlib import Path

    env_path = Path('.') / 'docker/.env'
    load_dotenv(env_path)
except Exception as ex:  # pylint: disable=broad-except
    pass

application = create_app(os.getenv('APP_ENV') or 'dev')
application.register_blueprint(blueprint)
application.app_context().push()
cors = CORS(application, resources={r"/*": {"origins": "*"}})


if __name__ == '__main__':
    application.run()
