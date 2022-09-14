from flask import request
from flask_restx import Resource, Namespace

from app.container import book_service
from app.dao.model.book import BookSchema

book_ns = Namespace('books')

books_schema = BookSchema(many=True)
book_schema = BookSchema()


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_books = book_service.get_all()
        return books_schema.dump(all_books), 200

    def post(self):
        data = request.json
        book_service.add_new(data)
        return '', 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        try:
            book = book_service.get_one(bid)
            return book_schema.dump(book), 200
        except Exception:
            return '', 404

    def put(self, bid):
        data = request.json
        data['id'] = bid
        book_service.update(data)
        return '', 204

    def patch(self, bid):
        data = request.json
        data['id'] = bid
        book_service.update_partial()
        return '', 204

    def delete(self, bid):
        book_service.delete(bid)
        return '', 204
