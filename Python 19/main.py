from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import forms

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '(/("ZOHDAJK)()kafau029)ÖÄ:ÄÖ:"OI§)"Z$()&"()!§(=")/$'

db = SQLAlchemy(app)


class MyTable(db.Model):
    __tablename__ = 'my_table'
    id = db.Column(db.Integer, primary_key=True)
    my_column = db.Column(db.String(100), nullable=False)


db.create_all()


class NewHome(Resource):
    def get(self):
        return {'response': 'Hello World'}


api.add_resource(NewHome, '/new_home')


@app.route('/')
def home():
    return jsonify({'response': '\Hello World"!'})


@app.route('/add_record', methods=['POST'])
def add_record():
    print(request)
    new_record = MyTable(my_column=request.form.get('my_column'))
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'status': 'ok'})


@app.route('/get_records')
def get_records():
    data = MyTable.query.all()
    data_new = [{'id': row.id, 'my_column': row.my_column} for row in data]
    return jsonify(data_new)


if __name__ == '__main__':
    app.run(debug=True)
