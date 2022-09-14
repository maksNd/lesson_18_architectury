from flask import request
from flask_restx import Resource, Namespace

from app.container import author_service
from app.database import db
from app.dao.model.author import AuthorSchema

author_ns = Namespace('authors')

authors_schema = AuthorSchema(many=True)
author_schema = AuthorSchema()


@author_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        all_authors = author_service.get_all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        data = request.json
        author_service.add_new(data)
        return '', 201


@author_ns.route('/<int:aid>')
class AuthorView(Resource):
    def get(self, aid):
        try:
            author = author_service.get_one(aid)
            return author_schema.dump(author), 200
        except Exception:
            return '', 404

    def put(self, aid):
        data = request.json
        data['id'] = aid
        author_service.update(data)
        return '', 204

    def patch(self, aid):
        data = request.json
        data['id'] = aid
        author_service.update_partial(data)
        return '', 204

    def delete(self, aid):
        author_service.delete(aid)
        return '', 204
