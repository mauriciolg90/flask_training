from db_config import Book, session

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
@app.route('/books', methods=['GET'])
def show_books():
    books = session.query(Book).all()
    # Return a key called 'books' that contains a list of books
    return jsonify(books=[b.serialize for b in books])

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