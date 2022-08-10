from flask import Flask
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '(/("ZOHDAJK)()kafau029)ÖÄ:ÄÖ:"OI§)"Z$()&"()!§(=")/$'
db = SQLAlchemy(app)

from python_22.models import User, MyTable

login_manager = LoginManager(app)
login_manager.login_view = 'sign_in'
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'info'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


admin = Admin(app)


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(MyTable, db.session))

bcrypt = Bcrypt(app)

from python_22 import routes
