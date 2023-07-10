from flask_admin import Admin
from src.admin.base import CustomAdminIndexView, SecureModelView, AdminIndexView
from src.admin.user import UserView
from src.admin.term import TermView
from src.admin.subject import SubjectView


admin = Admin(name="ადმინ პანელი",template_mode="bootstrap4", index_view=CustomAdminIndexView())