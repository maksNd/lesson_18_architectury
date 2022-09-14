from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import Author, AuthorSchema

author_ns = Namespace('authors')

authors_schema = AuthorSchema(many=True)
author_schema = AuthorSchema()


@author_ns.route('/')
class AuthorView(Resource):
    def get(self):
        all_books = db.session.query(Author).all()
        return authors_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_book = Author(**req_json)
        with db.session.begin():
            db.session.add(new_book)
        return '', 201
