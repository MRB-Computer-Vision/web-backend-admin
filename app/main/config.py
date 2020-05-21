# pylint: disable=missing-module-docstring
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ All configs independent of the environment
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """ All configs to DevelopmentConfig
    """
    DEBUG = True
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(
        user=os.getenv('DB_USERNAME'),
        pw=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        db=os.getenv('DB_DATABASE'))
    SQLALCHEMY_DATABASE_URI = DB_URL
    
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')


class TestingConfig(Config):
    """ All configs to TestingConfig
    """
    try:
        from flask.cli import load_dotenv
        from pathlib import Path

        env_path = Path('.') / 'docker/.env'
        load_dotenv(env_path)
    except Exception as ex:  # pylint: disable=broad-except
        pass

    DEBUG = True
    TESTING = True
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(
        user=os.getenv('DB_USERNAME'),
        pw=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        db=os.getenv('DB_DATABASE_TEST'))
    SQLALCHEMY_DATABASE_URI = DB_URL
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    """ All configs to ProductionConfig
    """
    DEBUG = False

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(
        user=os.getenv('DB_USERNAME'),
        pw=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        db=os.getenv('DB_DATABASE'))
    SQLALCHEMY_DATABASE_URI = DB_URL


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
