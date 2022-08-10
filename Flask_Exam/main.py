"""
Uzduotys:
1.(3) Surasti, isvardinti ir pataisyti visas projekte rastas klaidas zemiau, uz bent 5 rastas ir pataisytas pilnas balas:
    a) Registruojant naują vartotoją trūko pavardės lauko. DB jo reikalavo.
    b) Registruojant naują varototją gaunama AttributeError: 'User' object has no attribute 'is_active' klaida
    c) Paspaudus "Account Information" kyla jinja2.exceptions.UndefinedError: 'form_in_html' is undefined klaida
    d) Neveikė vartotojo atsijungimas
    e) Neveikė prisijungimas su registruotu vartotoju (Method Not Allowed)
    f) Neveikė prisijungimas su registruotu vartotoju (User or password does not match)
    g) Atnaujinant registruoto vartotojo informaciją neteisingai panaudotas POST HTTP metodas
    h) Neteisingai užpildomi numatytieji duomenys "Account Information" puslapyje
    i) user first_name tarp DB buvo integer tipo
    j) Kuriant vartotoją iš Admin puslapio, slaptažodis nebuvo šifruojamas
    ...
2.(7) Praplesti aplikacija i bibliotekos resgistra pagal apacioje surasytus reikalavimus:
    a)(1) Naudojant SQLAlchemy klases, aprasyti lenteles Book, Author su pasirinktinais atributais su tinkamu rysiu -
        vienas autorius, gali buti parases daug knygu, ir uzregistruoti juos admin'e
    b)(2) Sukurti (papildomus) reikiamus rysius tarp duombaziniu lenteliu, kad atitiktu zemiau pateiktus reikalavimus
    c) Sukurti puslapius Available Books ir My Books:
        i)(2) Available Books puslapis
            - isvesti bent knygos pavadinima ir autoriu
            - turi buti prieinamas tik vartotojui prisijungus,
            - rodyti visas knygas, kurios nera pasiskolintos
            - tureti mygtuka ar nuoroda "Borrow" prie kiekvienos knygos, kuri/ia paspaudus, knyga yra priskiriama
              varototojui ir puslapis perkraunamas
              (del paprastumo, sakome kad kiekvienos i sistema suvestos knygos turima lygiai 1)
        ii)(2) My Books puslapis
            - turi matytis ir buti prieinamas tik vartotojui prisijungus
            - rodyti visas knygas, kurios yra pasiskolintos prisijungusio vartotojo
            - salia kiekvienos knygos mygtuka/nuoroda "Return", kuri/ia paspaudus, knyga grazinama i biblioteka ir
              perkraunamas puslapis
    f)(2) Bonus: praplesti aplikacija taip, kad bibliotekoje kiekvienos knygos galetu buti
        daugiau negu vienas egzempliorius
Pastabos:
    - uzstrigus su pirmaja uzduotimi, galima paimti musu paskutini flask projekto template
        ir ten atlikti antra uzduoti
    - nereikalingus templates geriau panaikinti ar persidaryti, kaip reikia. Tas pats galioja su MyTable klase
    - antram vartotojui prisijungus, nebeturi matytis kyngos, kurios buvo pasiskolintos pirmojo vartotojo
        nei prie Available Books, nei prie My Books
    - visam administravimui, pvz. knygu suvedidimui galima naudoti admin
    - sprendziant bonus uzduoti, apsvarstyti papildomos lenteles isivedima
"""

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import AnonymousUserMixin, LoginManager, login_user, current_user, login_required, UserMixin, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from datetime import datetime
import forms

app = Flask(__name__)


class MyAnonymousUserMixin(AnonymousUserMixin):
    is_admin = False


login_manager = LoginManager(app)

login_manager.login_view = 'sign_in'
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'info'
login_manager.anonymous_user = MyAnonymousUserMixin

admin = Admin(app)

bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SECRET_KEY'] = '(/("ZOHDAJK)()kafau029)GrazinsiuSkolaEdziuiKaiGausiuAlgaÖÄ:ÄÖ:"OI§)"Z$(0)&"()!§(=")/$'

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    max_count = db.Column(db.Integer, nullable=False)
    db.UniqueConstraint('name', 'author_id')
    author = db.relationship('Author', backref='book')

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name


class BorrowedBook(db.Model):
    __tablename__ = 'borrowed_book'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrow_time = db.Column(db.Date, nullable=False)
    return_time = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book = db.relationship('Book', backref='book')
    user = db.relationship('User', backref='user')


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __unicode__(self):
        return self.email_address

    def __repr__(self):
        return self.email_address


db.create_all()


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_admin


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Book, db.session))
admin.add_view(MyModelView(Author, db.session))
admin.add_view(MyModelView(BorrowedBook, db.session))


@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return bcrypt.generate_password_hash(value).decode()
    return value


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


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


@app.route('/available_books', methods=['GET', 'POST'])
@login_required
def available_books():
    # form = forms.AvailableBooks()
    q = db.session.query(Book.name.label("book_name"),  Author.name.label("author_name"),
                         Book.id.label("book_id"),
                         (Book.max_count - db.func.sum(db.case([((BorrowedBook.return_time.is_(None) &
                                                                  (BorrowedBook.borrow_time != None)), 1)],
                                                               else_=0))).label("available")) \
        .join(Author, Author.id == Book.author_id)\
        .join(BorrowedBook, BorrowedBook.book_id == Book.id, isouter=True)
    # e = q.filter(BorrowedBook.book_id == 1)
    g = q.group_by(Book.id, Author.id)
    f = g.having(Book.max_count - db.func.sum(db.case([((BorrowedBook.return_time.is_(None) &
                                                         (BorrowedBook.borrow_time != None)), 1)], else_=0)) > 0)

    if request.method == 'POST':
        borrowed_book_id = request.form['btn_identifier']

        borrowed_book = BorrowedBook(
            book_id=borrowed_book_id,
            borrow_time=datetime.date(datetime.now()),
            user_id=current_user.id
        )
        db.session.add(borrowed_book)
        db.session.commit()

    data = f.all()
    return render_template('available_books.html', data=data)


@app.route('/my_books', methods=['GET', 'POST'])
@login_required
def my_books():
    q = db.session.query(Book.name.label("book_name"), Author.name.label("author_name"),
                         BorrowedBook.id.label("borrowed_book_id"),
                         BorrowedBook.borrow_time.label("borrow_time"))\
        .join(Author, Author.id == Book.author_id) \
        .join(BorrowedBook, BorrowedBook.book_id == Book.id)
    e = q.filter(BorrowedBook.return_time.is_(None))
    f = e.filter(BorrowedBook.user_id == current_user.id)
    g = f.order_by(BorrowedBook.borrow_time, Book.id, Author.id)

    if request.method == 'POST':
        borrowed_book_id = request.form['btn_identifier']

        borrowed_book = db.session.query(BorrowedBook).filter(BorrowedBook.id == borrowed_book_id).first();
        borrowed_book.return_time = datetime.date(datetime.now())
        # db.session.update(borrowed_book)
        db.session.commit()

    data = g.all()
    return render_template('my_books.html', data=data)


@app.route('/sign_out')
def sign_out():
    logout_user()
    flash('Goodbye, see you next time', 'success')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
