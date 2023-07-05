from sqlalchemy import func
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired

from src.admin.base import SecureModelView


class TermView(SecureModelView):

    create_modal = True
    edit_modal = True
    column_editable_list = ["description", "eng_word", "geo_word", "example", "photo"]
    column_searchable_list = ["description", "eng_word", "geo_word"]


    def get_query(self):
        return self.session.query(self.model)

    def get_count_query(self):
        return self.session.query(func.count("*"))