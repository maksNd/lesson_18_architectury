from app.dao.model.author import Author


class AuthorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Author).get(aid)

    def get_all(self):
        return self.session.query(Author).all()

    def add_new(self, data):
        author = Author(**data)
        self.session.add(author)
        self.session.commit()

    def update(self, author):
        self.session.add(author)
        self.session.commit()

    def delete(self, aid):
        author = self.get_one(aid)
        self.session.delete(author)
        self.session.commit()
