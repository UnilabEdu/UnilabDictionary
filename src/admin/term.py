from sqlalchemy import func
from flask import flash

from src.admin.base import SecureModelView
from src.extensions import ckeditor

class TermView(SecureModelView):

    create_modal = True
    edit_modal = True
    column_list = ["subject", "eng_word", "geo_word","description"]
    column_labels = {"subject":"მიმართულება", "eng_word": "სიტყვა eng","geo_word" : "სიტყვა ქართ","description":"განმარტება", "parent_word_rel":"მშობელი ტერმინი", "example": "მაგალითი"}
    column_editable_list = [ "subject","eng_word", "geo_word","description"]
    column_searchable_list = ["description", "eng_word", "geo_word"]
    form_excluded_columns = ["parent_word"]
    form_overrides =dict(example=ckeditor.CKEditorField('example'), description=ckeditor.CKEditorField('description'))

    page_size = 10




