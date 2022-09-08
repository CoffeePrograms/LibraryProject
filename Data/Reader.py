from datetime import datetime, date

from Service.ListService import get_item_by_id, get_index_by_id


class Reader:
    """ Читатель """

    # region Fields
    # Приватные поля
    # Номер читательского билета
    __id: str
    __fio: str
    __birthdate: date
    __telephone: str
    __books: []

    # Публичное поле
    __total = 0

    # endregion

    def __init__(self, id_reader=__total, fio="", birthdate=date(1900, 1, 1), telephone="", books=None):
        self.__total += 1
        self.__id = str(id_reader)
        self.__fio = fio
        self.__birthdate = birthdate
        self.__telephone = telephone
        if books is None:
            self.__books = []
        else:
            self.__books = books

    def __del__(self):
        self.__books = None

    # region Methods for properties
    @property
    def id(self):
        """ Идентификатор """
        return self.__id

    @property
    def fio(self):
        """ ФИО """
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value

    @property
    def age(self):
        """ Вычисление возраста """
        return int((datetime.now().date() - self.__birthdate).days / 365)

    @property
    def birthdate(self):
        """ Дата рождения """
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value):
        self.__birthdate = value

    @property
    def telephone(self):
        """ Номер телефона """
        return self.__telephone

    @telephone.setter
    def telephone(self, value):
        self.__telephone = value

    @property
    def books(self):
        """ Одолженные книги """
        return self.__books

    @books.setter
    def books(self, value):
        self.__books = value

    # endregion

    # region Methods
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

    def __str__(self):
        return f"Читательский билет: {self.__id}\nФИО: {self.__fio}\nВозраст: {self.age}\n" \
               f"Дата рождения: {self.__birthdate}\nНомер телефона: {self.__telephone}\n"

    def copy(self):
        reader: Reader
        reader = Reader(self.__id)
        reader.fio = self.__fio
        reader.birthdate = self.__birthdate
        reader.telephone = self.__telephone
        return reader
    # endregion
