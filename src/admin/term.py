from sqlalchemy import func

from src.admin.base import SecureModelView


class TermView(SecureModelView):

    create_modal = True
    edit_modal = True
    column_list = ["subject_name", "eng_word", "geo_word","description"]
    column_labels = {"subject_name":"მიმართულება", "eng_word": "სიტყვა eng","geo_word" : "სიტყვა ქართ","description":"ახსნა"}
    column_editable_list = ["subject_name", "eng_word", "geo_word","description"]
    column_searchable_list = ["subject_name","description", "eng_word", "geo_word"]


    def get_query(self):
        return self.session.query(self.model)

    def get_count_query(self):
        return self.session.query(func.count("*"))