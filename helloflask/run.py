# Get Python libraries/packages
from flask import Flask, request, render_template, session, g
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

# Variables


# Functions


# Flask app


app = Flask(__name__)

app.config.update(
    SECRET_KEY='topsecret',
    # SQLALCHEMY_DATABASE_URI='<database>://<user_id>:<password>@<server>/<database_name>',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:test1234@localhost/postgres',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
db = SQLAlchemy(app)


@app.before_request
def some_function():
    g.string = '<br> This code ran before any requests'


@app.route('/index')  # Home page
@app.route('/')
def hello_world():
    return "Hello, world! <br>" + g.string


# General GET request
@app.route('/new/')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is : {0} </h1>'.format(query_val) + g.string


# GET request without query
@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='Jack'):
    return '<h1> hello there! {} </h1>'.format(name)


# GET request strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> Here is a string: ' + name + '</h1>'


# GET request numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> The number you picked is : ' + str(num) + '</h1>'


# GET request add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> The sum is : {}'.format(num1 + num2) + '</h1>'


# GET request floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> The product is : {}'.format(num1 * num2) + '</h1>'


# Using Templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


# Jinja Templates
@app.route('/watch')
def movies_2017():
    movie_list = [
        'Autopsy of Jane Doe',
        'Ghost in a Shell',
        'Kong: Skull Island',
        'John Wick 2',
        'Spiderman - Homecoming'
    ]

    return render_template('movies.html', movies=movie_list, name='Jack')


# Tables
@app.route('/tables')
def movies_plus():
    movie_dict = {
        'Autopsy of Jane Doe': 02.14,
        'Ghost in a Shell': 3.20,
        'Kong: Skull Island': 1.50,
        'John Wick 2': 02.52,
        'Spiderman - Homecoming': 1.48
    }

    return render_template('table-data.html', movies=movie_dict, name='Sally')


# Filters
@app.route('/filters')
def filter_data():
    movie_dict = {
        'Autopsy of Jane Doe': 02.14,
        'Ghost in a Shell': 3.20,
        'Kong: Skull Island': 1.50,
        'John Wick 2': 02.52,
        'Spiderman - Homecoming': 1.48
    }

    return render_template('filter-data.html', movies=movie_dict, name='None', film='a christmas carol')


# Macros
@app.route('/macros')
def jinja_macros():
    movie_dict = {
        'Autopsy of Jane Doe': 02.14,
        'Ghost in a Shell': 3.20,
        'Kong: Skull Island': 1.50,
        'John Wick 2': 02.52,
        'Spiderman - Homecoming': 1.48
    }

    return render_template('using-macros.html', movies=movie_dict)


# Session
@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'Jack'
    return render_template('session.html', session=session, name=session['name'])



class Publication(db.Model):

    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Publisher is {}'.format(self.name)


class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)