from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db
from src.models.base import BaseModel

class User(db.Model, BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.String, nullable=False)

    # role_id = db.Column(db.ForeignKey("roles.id"))
    # role = db.relationship("Role", back_populates="user")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.name} {self.surname}"


# class Role(db.Model):
#
#     __tablename__ = "roles"
#     id = db.Column(db.Integer, primary_key=True)
#     role = db.Column(db.String, unique=True)
#
#     def __repr__(self):
#         return f"{self.name}"
