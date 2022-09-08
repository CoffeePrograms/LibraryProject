from datetime import datetime
from json import JSONEncoder

from Data.Book import Book
from Data.Reader import Reader


class CustomEncoder(JSONEncoder):
    def default(self, value):
        import datetime
        if isinstance(value, datetime.date):
            return dict(year=value.year, month=value.month, day=value.day)
        else:
            return value.__dict__


def reader_from_string(json_dct):
    id_reader = json_dct['_Reader__id']
    fio = json_dct['_Reader__fio']
    birthdate = json_dct['_Reader__birthdate']
    telephone = json_dct['_Reader__telephone']
    books_json = json_dct['_Reader__books']
    books = []
    for index in books_json:
        books.append(index)
    return Reader(id_reader, fio, birthdate, telephone, books)


def book_from_string(json_dct):
    id_book = json_dct['_Book__id']
    title = json_dct['_Book__title']
    author = json_dct['_Book__author']
    genre = json_dct['_Book__genre']
    age_mark = json_dct['_Book__age_mark']
    count = json_dct['_Book__count']
    return Book(id_book, title, author, genre, age_mark, count)


def library_from_string(json_dct):
    books = json_dct['_LibraryHandler__books']
    readers = json_dct['_LibraryHandler__readers']
    from Handler.LibraryHandler import LibraryHandler
    return LibraryHandler(books, readers)


def library_hook_for_read_json(json_dct):
    if '_Book__id' in json_dct.keys():
        return book_from_string(json_dct)
    elif '_Reader__id' in json_dct.keys():
        return reader_from_string(json_dct)
    elif '_LibraryHandler__books' in json_dct.keys():
        return library_from_string(json_dct)
    elif 'year' in json_dct.keys():
        return datetime.strptime(f"{json_dct['year']}-{json_dct['month']}-{json_dct['day']}", "%Y-%m-%d").date()
    else:
        return json_dct
