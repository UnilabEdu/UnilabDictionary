from sqlalchemy import func
from wtforms import SelectField
from flask import flash

from src.admin.base import SecureModelView


class TermView(SecureModelView):

    create_modal = True
    edit_modal = True
    column_list = ["subject", "eng_word", "geo_word","description"]
    column_labels = {"subject":"მიმართულება", "eng_word": "სიტყვა eng","geo_word" : "სიტყვა ქართ","description":"განმარტება", "parent_word_rel":"მშობელი ტერმინი"}
    column_editable_list = [ "subject","eng_word", "geo_word","description"]
    column_searchable_list = ["description", "eng_word", "geo_word"]
    form_excluded_columns = ["parent_word"]

    page_size = 10




