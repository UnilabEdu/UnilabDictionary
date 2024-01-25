from sqlalchemy import func
from flask import Markup


from src.admin.base import SecureModelView


class SubjectView(SecureModelView):

    create_modal = True
    edit_modal = True
    can_edit = True
    column_editable_list = ["name"]
    column_labels = {"terms": "ტერმინი","name": "მიმართულების სახელი", "course_link": "კურსის ლინკი", "internship_link": "სტაჟირების ლინკი"}
    column_searchable_list = ["name", "course_link", "internship_link"]
    column_formatters = {
                        'course_link': lambda v, c, m, p: Markup(f'<a href={m.course_link}>{"ლინკი"}</a>'),
                        'name': lambda v, c, m, p: m.name if m.name else '-',
                         'internship_link': lambda v, c, m, p: Markup(f'<a href={m.internship_link}>{"ლინკი"}</a>'),
                        }
    page_size = 10


