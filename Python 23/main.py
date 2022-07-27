from flask import Flask, render_template, redirect, url_for, flash, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
import forms

app = Flask(__name__)
login_manager = LoginManager(app)

login_manager.login_view = 'sign_in'
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'info'

admin = Admin(app)

bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '(/("ZOHDAJK)()kafau029)ÖÄ:ÄÖ:"OI§)"Z$()&"()!§(=")/$'

db = SQLAlchemy(app)


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


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_admin


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(MyTable, db.session))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_form', methods=['GET', 'POST'])
def add_form():
    form = forms.AddForm()
    if form.validate_on_submit():
        my_table = MyTable(my_column=form.my_column.data)
        db.session.add(my_table)
        db.session.commit()
        return render_template('success.html')
    return render_template('add_form.html', form=form)


@app.route('/show')
@login_required
def show():
    data = MyTable.query.all()
    return render_template('show.html', data=data)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password1.data).decode()
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email_address=form.email_address.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Welcome, {current_user.first_name}', 'success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email_address=form.email_address.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'Welcome, {current_user.first_name}', 'success')
            return redirect(request.args.get('next') or url_for('home'))
        flash(f'User or password does not match', 'danger')
        return render_template('sign_in.html', form=form)
    return render_template('sign_in.html', form=form)


@app.route('/update_account_information', methods=['GET', 'POST'])
def update_account_information():
    form = forms.UpdateAccountInformationForm()
    if request.method == 'GET':
        form.email_address.data = current_user.email_address
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    if form.validate_on_submit():
        current_user.email_address = form.email_address.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash('User information updated', 'success')
        return redirect(url_for('update_account_information'))
    return render_template('update_account_information.html', form=form)


@app.route('/sign_out')
def sign_out():
    logout_user()
    flash('Goodbye, see you next time', 'success')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
