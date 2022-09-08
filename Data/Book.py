class Book:
    """ Книга """

    # region Fields
    # Приватные поля
    __id: int
    __title: str
    __author: str
    __genre: str
    # Возрастной рейтинг
    __age_mark: int
    __count: int

    # endregion

    def __init__(self, id_book, title="", author="", genre="", age_mark=0, count=0):
        self.__id = int(id_book)
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__age_mark = age_mark
        self.__count = count

    # region Properties
    @property
    def id(self):
        """ Идентификатор """
        return self.__id

    @property
    def title(self):
        """ Название """
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        """ Автор """
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def genre(self):
        """ Жанр """
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def age_mark(self):
        """ Возрастной рейтинг """
        return self.__age_mark

    @age_mark.setter
    def age_mark(self, value):
        self.__age_mark = value

    @property
    def count(self):
        """ Кол-во книг в наличии """
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

    # endregion
    # region Methods
    def __str__(self):
        return f"Ид: {self.__id}\nНазвание: \"{self.__title}\"\nАвтор: {self.author}\nЖанр: {self.__genre}\n" \
               f"Возростной рейтинг: {self.__age_mark}+\nВ наличии (шт.): {self.__count}"

    def copy(self):
        book: Book
        book = Book(self.__id)
        book.title = self.__title
        book.author = self.__author
        book.genre = self.__genre
        book.age_mark = self.__age_mark
        book.count = self.__count
        return book
    # endregion
