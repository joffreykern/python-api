import flask
import jsonpickle
from flask import request
from flask.json import JSONEncoder

from models.book import Book


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return JSONEncoder.default(self, obj)


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = CustomJSONEncoder

books = [
    Book(0, 'A Fire Upon the Deep', 'Vernor Vinge', '1992'),
    Book(1, 'The Ones Who Walk Away From Omelas', 'Ursula K. Le Guin', '1973'),
    Book(2, 'Dhalgren', 'Samuel R. Delany', '1975')
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World</h1>"


@app.route('/api/v1/books', methods=['GET'])
def get_books():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return jsonpickle.encode(books)

    book = (list(filter(lambda x: x.id == id, books)))
    return jsonpickle.encode(book)


app.run()
