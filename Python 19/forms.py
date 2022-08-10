from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    my_column = StringField('My Column', [DataRequired()])
    submit = SubmitField('Submit')
