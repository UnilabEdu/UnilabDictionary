from sqlalchemy import func

from src.admin.base import SecureModelView


class SubjectView(SecureModelView):

    create_modal = True
    edit_modal = True
    column_editable_list = ["name", "course_link", "internship_link"]
    column_labels = {"name": "მიმართულების სახელი", "course_link": "კურსის ლინკი", "internship_link": "სტაჟირების ლინკი"}
    column_searchable_list = ["name", "course_link", "internship_link"]

    def get_query(self):
        return self.session.query(self.model)

    def get_count_query(self):
        return self.session.query(func.count("*"))
