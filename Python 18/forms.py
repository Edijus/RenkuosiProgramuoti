from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from main import app
from main import Product


class ProductForm(FlaskForm):
    code = StringField('Code', [DataRequired()])
    name = StringField('Name', [DataRequired()])
    weight = IntegerField('Weight', [DataRequired()])
    submit = SubmitField('Submit')


class StockForm(FlaskForm):
    quantity = IntegerField('Quantity', [DataRequired()])
    product = QuerySelectField(query_factory=Product.query.all, allow_blank=True, get_label="name",
                               get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')
