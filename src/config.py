from os import path, environ


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static/uploads")

    SECRET_KEY = environ.get("SECRET_KEY")
    if environ.get("FLASK_ENV") == "development":
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(BASE_DIRECTORY, "database.db")
    else:
        DB_USER = environ.get("DB_USER")
        DB_PASS = environ.get("DB_PASS")
        SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@217.147.233.61/postgres"

    CKEDITOR_PKG_TYPE = 'basic'