from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static/uploads")

    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")

    CKEDITOR_PKG_TYPE = 'basic'