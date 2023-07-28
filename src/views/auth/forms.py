from flask_wtf import FlaskForm
from src.models.base import BaseModel
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from src.models import User

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("რეგისტრაცია")
    def validate_username(self, field):
        existing_user = User.query.filter_by(username=field.data).first()
        if existing_user:
            raise ValidationError("ეს იუზერნეიმი უკვე გამოყენებულია")
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("ავტორიზაცია")

