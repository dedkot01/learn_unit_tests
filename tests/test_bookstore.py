from unittest.mock import Mock

from my_pck import Bookstore


def test_display_book_info():
    book_mock = Mock()
    book_mock.title = "Моби Дик"
    book_mock.author = "Герман Мелвилл"
    book_mock.price = 150

    # Создали объект класса Bookstore и передали в него мок-объект
    bookstore = Bookstore(book_mock)

    # Протестировали метод display_book_info()
    assert bookstore.display_book_info() == "Название: Моби Дик, Автор: Герман Мелвилл, Цена: 150"
