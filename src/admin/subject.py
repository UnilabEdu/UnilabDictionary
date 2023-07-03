from sqlalchemy import func
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired

from src.admin.base import SecureModelView

class SubjectView(SecureModelView):
    create_modal = True
    edit_modal = True
    column_editable_list = ["name", "course_link", "internship_link"]
