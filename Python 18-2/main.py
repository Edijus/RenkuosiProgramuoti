from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'iohYIUJk651KJH'
db = SQLAlchemy(app)

grade_student = db.Table('grade_student', db.metadata,
                         db.Column('grade_id', db.Integer, db.ForeignKey('grade.id')),
                         db.Column('student_id', db.Integer, db.ForeignKey('student.id')))


class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    students = db.relationship('Student', secondary=grade_student, back_populates='grades')


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(1000), nullable=False)
    last_name = db.Column(db.String(1000), nullable=False)
    grades = db.relationship('Grade', secondary=grade_student, back_populates='students')


db.create_all()

@app.route('/')
def index():
    return redirect(url_for('home_page'))


@app.route('/my_home')
def home_page():
    return render_template('index.html')


@app.route('/addgrade', methods=['GET', 'POST'])
def add_grade():
    form = forms.AddGradeForm()
    if form.validate_on_submit():
        grade = Grade(grade=form.grade.data)
        db.session.add(grade)
        db.session.commit()
    return render_template('add_grade.html', form_in_html=form)


@app.route('/addstudent', methods=['GET', 'POST'])
def add_student():
    form = forms.AddStudentForm()
    if form.validate_on_submit():
        student = Student(first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(student)
        db.session.commit()
    return render_template('add_student.html', form_in_html=form)


@app.route('/addstudentgrade', methods=['GET', 'POST'])
def add_student_grade():
    form = forms.AddStudentGradesForm()
    if form.validate_on_submit():
        student = Student.query.get(form.student.data.id)
        for grade in form.grades.data:
            grade_obj = Grade.query.get(grade.id)
            student.grades.append(grade_obj)
        db.session.add(student)
        db.session.commit()
        return render_template('add_student_grade.html', form_in_html=form)
    return render_template('add_student_grade.html', form_in_html=form)


if __name__ == '__main__':
    app.run(debug=True)
