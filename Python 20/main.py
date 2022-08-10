from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '(/("ZOHDAJK)()kafau029)ÖÄ:ÄÖ:"OI§)"Z$()&"()!§(=")/$'

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = 'my_table'
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        my_user = User(email_address=form.email_address.data, password=form.password1.data)
        db.session.add(my_user)
        db.session.commit()
        login_user(my_user)
        return render_template('success.html')
    return render_template('sign_up.html', form_in_html=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignInForm()
    if form.validate_on_submit():
        my_user = User.query.filter_by(email_address=form.email_address.data).first()
        if my_user is None:
            return render_template('sign_in.html', form_in_html=form, message='User does not exist')
        elif my_user.password == form.password.data:
            login_user(my_user)
            return render_template('success.html')
        return render_template('sign_in.html', form_in_html=form, message='Wrong password')
    return render_template('sign_in.html', form_in_html=form)


@app.route('/sign_out')
def sign_out():
    logout_user()
    return render_template('home.html')


@app.route('/show')
def show():
    return render_template('show.html')


if __name__ == '__main__':
    app.run(debug=True)
