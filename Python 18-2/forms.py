from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import main


class AddGradeForm(FlaskForm):
    grade = IntegerField('Grade', [DataRequired()])
    submit = SubmitField('Add Grade')


class AddStudentForm(FlaskForm):
    first_name = StringField('First name', [DataRequired()])
    last_name = StringField('Last name', [DataRequired()])
    submit = SubmitField('Add Student')


class AddStudentGradesForm(FlaskForm):
    student = QuerySelectField(query_factory=main.Student.query.all, get_label='first_name',
                               get_pk=lambda obj: str(obj))
    grades = QuerySelectMultipleField(query_factory=main.Grade.query.all, get_label="grade",
                                      get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit grade')
