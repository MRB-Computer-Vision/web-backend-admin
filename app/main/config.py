import os

basedir = os.path.abspath(os.path.dirname(__file__))

try:
    from flask.cli import load_dotenv
    from pathlib import Path

    env_path = Path('.') / 'docker/.env'
    load_dotenv(env_path)
except Exception as ex:
    pass


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{host}/{db}'.format(user=os.getenv('DB_USERNAME'),pw=os.getenv('DB_PASSWORD'),host=os.getenv('DB_HOST'),db=os.getenv('DB_DATABASE'))
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY