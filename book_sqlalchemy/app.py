from db_config import Book, session

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

# Landing page that will display all the books in our database
@app.route('/')
@app.route('/books')
def show_books():
    books = session.query(Book).all()
    return render_template("show_books.html", books=books)

# This will let us create a new book and save it in our database
@app.route('/books/add/', methods=['GET', 'POST'])
def add_book():
    # Validate method and not null fields for the book
    if request.method == 'POST' and request.form['title'] and request.form['author']:
        book = Book(
            title=request.form['title'],
            author=request.form['author'],
            genres=request.form['genres']
        )
        session.add(book)
        session.commit()
        return redirect(url_for('show_books'))
    else:
        return render_template('add_book.html')

# This will let us update our books and save it in our database
@app.route("/books/update/<int:book_id>", methods=['GET', 'POST'])
def update_book(book_id):
    book = session.query(Book).filter_by(id=book_id).one()
    # Validate method and not null fields for the book
    if request.method == 'POST' and request.form['title'] and request.form['author']:
        book.title = request.form['title']
        book.author = request.form['author']
        book.genres = request.form['genres']
        session.add(book)
        session.commit()
        return redirect(url_for('show_books'))
    else:
        return render_template('update_book.html', book=book)

# This will let us delete our book
@app.route('/books/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(book)
        session.commit()
        return redirect(url_for('show_books'))
    else:
        return render_template('delete_book.html', book=book)