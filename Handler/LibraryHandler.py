from datetime import datetime

from Data.BorrowedBook import BorrowedBook
from Service.ListService import get_item_by_id, get_index_by_id


class LibraryHandler:
    """ Обработчик для работы с книгами и читателями """

    def __init__(self, books=None, readers=None):
        if readers is None:
            readers = []
        if books is None:
            books = []
        self.__books = books
        self.__readers = readers

    # region Properties
    @property
    def books(self):
        """ Книги """
        return self.__books

    @property
    def readers(self):
        """ Читатели """
        return self.__readers

    # endregion

    # region Books
    def get_info_about_books(self) -> str:
        res = "--- Книги ---\n"
        for item in self.__books:
            res += item.__str__()
            res += "\n---\n"
        return res

    def add_book(self, book):
        self.books.append(book)

    def del_book(self, id_book) -> bool:
        book = get_item_by_id(self.__books, id_book)
        if book is None:
            print('Не найдена книга с указанным идентификатором')
            return False
        else:
            self.books.remove(book)
            return True

    def is_book_exists(self, id_book) -> bool:
        index_book = get_index_by_id(self.__books, id_book)
        if index_book == -1:
            return False
        else:
            return True

    def get_value_of_book_by_id(self, id_book):
        book = get_item_by_id(self.__books, id_book)
        return book.copy()

    def edit_book(self, id_book, book) -> bool:
        index_book = get_index_by_id(self.__books, id_book)
        if index_book == -1:
            print('Не найдена книга с указанным идентификатором')
            return False
        else:
            self.books[index_book] = book
            return True

    # endregion

    # region Readers
    def get_info_about_readers(self) -> str:
        res = "\n--- Читатели ---\n"
        for item in self.__readers:
            res += item.__str__()
            res += f"Взято книг: {len(item.books)}\n"
            res += "---\n"
        return res

    def add_reader(self, reader):
        self.readers.append(reader)

    def del_reader(self, id_reader):
        reader = get_item_by_id(self.readers, id_reader)
        self.readers.remove(reader)

    def is_reader_exists(self, id_reader) -> bool:
        index_reader = get_index_by_id(self.__readers, id_reader)
        if index_reader == -1:
            return False
        else:
            return True

    def get_value_of_reader_by_id(self, id_reader):
        reader = get_item_by_id(self.__readers, id_reader)
        return reader.copy()

    def edit_reader(self, id_reader, reader):
        index_reader = get_index_by_id(self.readers, id_reader)
        self.readers[index_reader] = reader

    # endregion

    # region Borrowed books
    def get_info_about_books_of_reader(self, id_reader) -> str:
        """
        Формирование строки с информацией по одолженным книгам

        :param self: библиотека
        :param id_reader: ид читателя
        :return: строка
        """
        index = get_index_by_id(self.__books, id_reader)
        reader = self.__readers[index]
        res = f"\n--- Книги читателя №{reader.id} ({reader.fio}) ---\n"
        for id_book in reader.books:
            index = get_index_by_id(self.__books, id_book)
            res += self.books[index].__str__()
        return res

    def took_book(self, reader, book, days=14):
        """
        Читатель одолживает книгу

        :param reader: читатель
        :param book: книга
        :param days: дни до возвращения книги
        """
        if book.count <= 0:
            print("Ошибка! В наличии нет свободных экземпляров")
        elif reader.age < book.age_mark:
            print("Ошибка! Возрастной рейтинг не позволяет выдать книгу данному читателю")
        else:
            reader.books.append(BorrowedBook(book.id, datetime.today().date(), None, days))
            book.count -= 1
            print("Книга записана на читателя")

    def returned_book(self, reader, id_book):
        """
        Возвращение книги

        :param reader: читатель
        :param id_book: ид книги
        """
        index = get_index_by_id(reader.books, id_book)
        if index == -1:
            print("У читателя нет указанной книги")
        else:
            del reader.books[index]
            book = get_item_by_id(self.books, id_book)
            book.count += 1
            print("Книга возвращена")

    # endregion

    def __str__(self):
        res = self.get_info_about_books()
        res += self.get_info_about_readers()
        return res
