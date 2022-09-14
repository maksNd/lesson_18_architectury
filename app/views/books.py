from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import Book, BookSchema

book_ns = Namespace('books')

books_schema = BookSchema(many=True)
book_schema = BookSchema()


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_books = db.session.query(Book).all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_book = Book(**req_json)
        with db.session.begin():
            db.session.add(new_book)
        return '', 201
