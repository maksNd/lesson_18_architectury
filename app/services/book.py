class BookService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def add_new(self, data):
        return self.dao.add_new(data)

    def update(self, data):
        bid = data.get('id')
        book = self.get_one(bid)
        book.name = data.get('name')
        book.year = data.get('year')
        self.dao.update(book)

    def update_partial(self, data):
        bid = data.get('id')
        book = self.get_one(bid)
        if 'name' in data:
            book.first_name = data.get('name')
        if 'year' in data:
            book.last_name = data.get('year')
        self.dao.update(book)

    def delete(self):
        ...
