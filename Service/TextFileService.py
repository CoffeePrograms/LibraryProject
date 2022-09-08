from datetime import datetime, date

from Data.Book import Book
from Data.BorrowedBook import BorrowedBook
from Data.Reader import Reader
from Handler.LibraryHandler import LibraryHandler


# region Write
def write_book_to_file(book):
    res = f"{book.id};{book.title};{book.author};{book.genre};{book.age_mark};{book.count}\n"
    return res


def write_reader_to_file(reader):
    res = f"{reader.id};{reader.fio};{reader.birthdate};{reader.telephone};"
    for i in range(0, len(reader.books)):
        res += f"{reader.books[i].id}!{reader.books[i].date_borrowed}!{reader.books[i].date_will_return}"
        if i != len(reader.books) - 1:
            res += ','
        else:
            res += '\n'
    return res


def write_library_to_string(library: LibraryHandler):
    res = "BBB\n"
    for item in library.books:
        res += write_book_to_file(item)
    res += "RRR\n"
    for item in library.readers:
        res += write_reader_to_file(item)
    return res + "\n"


# endregion

# region Read


def text_to_date(text: str) -> date:
    return datetime.strptime(text, "%Y-%m-%d").date()


def read_reader_from_string(lst):
    id_reader = lst[0]
    fio = lst[1]
    birthdate = text_to_date(lst[2])
    telephone = lst[3]
    books_str = lst[4].split(',')
    books = []
    for item in books_str:
        if item != "":
            books_lst = item.split('!')
            books.append(BorrowedBook(books_lst[0],
                                      text_to_date(books_lst[1]),
                                      text_to_date(books_lst[2])))
    return Reader(id_reader, fio, birthdate, telephone, books)


def read_readers_from_string(lst_str):
    readers = []
    for item in lst_str:
        lst = item.split(';')
        readers.append(read_reader_from_string(lst))
    return readers


def read_book_from_string(lst):
    id_book = int(lst[0])
    title = lst[1]
    author = lst[2]
    genre = lst[3]
    age_mark = int(lst[4])
    count = int(lst[5])
    return Book(id_book, title, author, genre, age_mark, count)


def read_books_from_string(lst_str):
    books = []
    for item in lst_str:
        lst = item.split(';')
        books.append(read_book_from_string(lst))
    return books


def read_library_from_string(text):
    text = text.split('\n')
    i_book = text.index('BBB')
    i_reader = text.index('RRR')
    books = read_books_from_string(text[i_book + 1:i_reader:])
    readers = read_readers_from_string(text[i_reader + 1:len(text) - 1:])
    return LibraryHandler(books, readers)
# endregion
