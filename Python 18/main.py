from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import forms

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'GrazinsiuSkolaEdziuiKaiGausiuAlga'

db = SQLAlchemy(app)

Migrate(app, db)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    stock = db.relationship('Stock', backref='product')


class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = forms.ProductForm()
    if form.validate_on_submit():
        product = Product(code=form.code.data, name=form.name.data, weight=form.weight.data)
        db.session.add(product)
        db.session.commit()
        return render_template('add_product.html', form=form, message='Success')
    return render_template('add_product.html', form=form)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    form = forms.StockForm()
    if form.validate_on_submit():
        stock = Stock(product_id=form.product.data.id, quantity=form.quantity.data)
        db.session.add(stock)
        db.session.commit()
        return render_template('add_stock.html', form=form, message='Success')
    return render_template('add_stock.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
