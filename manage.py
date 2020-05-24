import os
import unittest

from app import blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app.main.models import user
from app.main.models import blacklist
from app.main.models import exam
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

try:
    from flask.cli import load_dotenv
    from pathlib import Path

    env_path = Path('.') / 'docker/.env'
    load_dotenv(env_path)
except Exception as ex:  # pylint: disable=broad-except
    pass

app = create_app(os.getenv('APP_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
cors = CORS(app, resources={r"/*": {"origins": "*"}})

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
