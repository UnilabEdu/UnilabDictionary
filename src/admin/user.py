from wtforms.fields import PasswordField
from wtforms.validators import DataRequired, equal_to, ValidationError
from flask import flash

from src.admin.base import SecureModelView





class UserView(SecureModelView):
    can_create = False
    can_delete = False
    edit_modal = True

    form_excluded_columns = ('username')

    form_extra_fields = {"old_password": PasswordField("ძველი პაროლი", validators=[DataRequired()]),
                         "new_password": PasswordField("ახალი პაროლი", validators=[DataRequired()]),
                         "repeat_password": PasswordField("გაიმეორეთ ახალი პაროლი", validators=[DataRequired(), equal_to('new_password',
                                                                               message="პაროლები უნდა ემთხვეოდეს")])}


    def on_model_change(self, form, model, is_created):
        if model.check_password(form.old_password.data):
            model.password = form.new_password.data
        else:
            flash("ძველი პაროლი არ ემთხვევა")



