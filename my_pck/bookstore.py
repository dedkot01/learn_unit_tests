from . import Book


class Bookstore:
    def __init__(self, book: Book):
        self.book = book

    def display_book_info(self):
        return f"Название: {self.book.title}, Автор: {self.book.author}, Цена: {self.book.price}"
