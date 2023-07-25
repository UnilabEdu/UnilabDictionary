from flask import flash
from flask_admin.form.upload import ImageUploadField

from src.admin.base import SecureModelView
from flask_ckeditor import CKEditorField
from os import path

class TermView(SecureModelView):

    column_list = ["subject", "eng_word", "geo_word"]
    column_labels = {"subject":"მიმართულება", "eng_word": "სიტყვა eng","geo_word" : "სიტყვა ქართ","description":"განმარტება", "parent_word_rel":"მშობელი ტერმინი", "example": "მაგალითი"}
    column_editable_list = [ "subject","eng_word", "geo_word"]
    column_searchable_list = ["description", "eng_word", "geo_word","example"]

    form_excluded_columns = ["parent_word"]
    form_overrides = dict(description=CKEditorField, example=CKEditorField, img=ImageUploadField)
    form_args = {"img": {"label": "სურათის ატვირთვა","base_path": path.dirname("src/static/uploads"), "url_relative_path": "static/uploads"}}
    form_columns = ["subject","parent_word_rel","eng_word", "geo_word","description","example"]

    create_template ='admin/term/create.html'
    edit_template = 'admin/term/edit.html'

    page_size = 10

