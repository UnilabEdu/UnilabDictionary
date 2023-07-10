from src.admin.base import SecureModelView


class UserView(SecureModelView):

    can_create = False
    can_delete = False
    edit_modal = False

    column_searchable_list = ["username"]
    column_list = ["username", "role"]
    column_labels = {"username": "სახელი", "role": "ტიპი"}
