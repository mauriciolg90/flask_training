# For routing and queries on the model
from src.models.indicators import Indicators, session
from flask import Flask, jsonify, request

app = Flask(__name__)

"""
    Returns a list of countries filtering by:
        INDICATOR: SW_LIFS (Life satisfaction)
        INEQUALITY: TOT (Total)
        VALUE: greater than the input index
    Parameters:
        index: min threshold for filtering
"""
@app.route('/countries/sw_lifs_gt/<float:index>', methods=['GET'])
def countries_sw_lifs_gt(index):
    if index > 0:
        # Query on the database according to the filters
        countries = session.query(Indicators.location, Indicators.country).filter(
            Indicators.indicator_code == 'SW_LIFS',
            Indicators.inequality_code == 'TOT',
            Indicators.value > index
        ).all()
        # Return the results
        return jsonify(countries)
    else:
        return 'The index format is invalid!'

@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

"""
@app.route('/book/<int:book_id>', methods=['GET'])
def show_book(book_id):
    book = session.query(Book).filter_by(id=book_id).one_or_none()
    if book is not None:
        # Return a key called 'book' that contains just one book
        return jsonify(book=book.serialize)
    else:
        return 'The book with id {} does not exist!'.format(book_id)

@app.route('/book', methods=['POST'])
def add_book():
    #request.json['title']
    title = request.args.get('title', '')
    author = request.args.get('author', '')
    genres = request.args.get('genres', '')
    # Validate not null fields for the book
    if title and author:
        book = Book(title=title, author=author, genres=genres)
        session.add(book)
        session.commit()
        # Return a key called 'book' that contains the added book
        return jsonify(book=book.serialize)
    else:
        return 'Error trying to add a book! Please, check the params..'

@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    #request.json['title']
    title = request.args.get('title', '')
    author = request.args.get('author', '')
    genres = request.args.get('genres', '')
    book = session.query(Book).filter_by(id=book_id).one_or_none()
    # Validate book and not null fields for it
    if book is not None and title and author:
        book.title = title
        book.author = author
        book.genres = genres
        session.add(book)
        session.commit()
        # Return a key called 'book' that contains the updated book
        return jsonify(book=book.serialize)
    else:
        return 'Error trying to update the book! Please, check the params..'

@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).one_or_none()
    if book is not None:
        session.delete(book)
        session.commit()
        return 'The book with id {} was deleted'.format(book_id)
    else:
        return 'The book with id {} does not exist!'.format(book_id)
"""