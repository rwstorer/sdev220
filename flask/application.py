#import requests
#import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    
    def __repr__(self) -> str:
        return f"id {self.id}, book_name {self.book_name}, " + \
            f"author {self.author} publisher {self.publisher}"

@app.route('/books')
def get_books() -> str:
    """Get all the books in the DB

    Returns:
        str: a dictionary of all the books in the db
    """
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)

    return {'books': output}


@app.route('/books', methods=['POST'])
def create_book() -> str:
    """Create book data

    Returns:
        str: the book id created
    """
    book = Book()
    book.id = request.json['id']
    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}


# http://localhost:5000/books/1
@app.route('/books/<id>', method=['PUT'])
def update_book() -> str:
    """Update the book

    Returns:
        str: the updated book id
    """
    pass


# http://localhost:5000/books/1
@app.route('/books/<id>', method=['DELETE'])
def delete_book(id: int) -> str:
    """delete the book

    Returns:
        str: id of the deleted book
    """
    book = Book.query.get(id)
    ret_val: dict = {}
    if book is None:
        ret_val['error'] = f"Book: {id} not found."
    else:
        db.session.delete(book)
        db.session.commit()
        ret_val['success'] = f"Book: {id} deleted."
        
    return ret_val