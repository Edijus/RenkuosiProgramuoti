from flask_login import UserMixin
from python_22 import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    email_address = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)


class MyTable(db.Model):
    __tablename__ = 'my_table'
    id = db.Column(db.Integer, primary_key=True)
    my_column = db.Column(db.String(100), nullable=False)


db.create_all()

