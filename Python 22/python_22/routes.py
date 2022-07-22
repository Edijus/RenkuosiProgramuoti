from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from python_22 import forms, db, app, bcrypt
from python_22.models import User, MyTable


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
