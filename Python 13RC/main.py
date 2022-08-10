from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


# http://127.0.0.1:5000/path_param?query_key=query_value
@app.route('/<name>')  # Bet kas po slešo
def hello_name(name: str):
    print(request)
    return f'<h1>Hello, {name}!</h1>'


@app.route('/username', methods=['GET', 'POST'])
def enter_username():
    if request.method == 'POST':
        name = request.form.get('username')
        print(name)
    return render_template('template.html')


@app.route('/data')
def get_data():
    data = [1, 2, 3, 4]
    return render_template('data.html', data=data)


@app.route('/base_data')
def base_data():
    data = [10, 20, 30, 40, 50]
    return render_template('data.html', data=data)


app.run()
