import codecs
import json

from datetime import date
from enum import Enum

from Data.Book import Book
from Data.Reader import Reader
from Data.BorrowedBook import BorrowedBook
from Handler.LibraryHandler import LibraryHandler
from Service.JsonService import CustomEncoder, library_hook_for_read_json
from Service.ListService import get_index_by_id, get_item_by_id
from Service.TextFileService import write_library_to_string, read_library_from_string, text_to_date


class FileType(Enum):
    TXT = 1
    JSON = 2


def main_menu():
    """
    Главное меню программы
    """

    file_type = choice_file_type()
    if file_type is None:
        return
    data = load_data(file_type)
    choice_category(data)
    save_data(file_type, data)


# region Work with file
def choice_file_type() -> FileType | None:
    file_type = None
    is_processed = False
    while is_processed is False:
        print("Выберите в файле какого формата, будут храниться данные")
        print("1 - Работать с текстовым файлом")
        print("2 - Работать с json файлом")
        print("0 - Выход")
        option = input(">> ")
        match option:
            case "1":
                file_type = FileType.TXT
                print("Выбран текстовый файл")
                is_processed = True

            case "2":
                file_type = FileType.JSON
                print("Выбран json файл")
                is_processed = True

            case "0":
                return None

            case _:
                print("Не найден указанный пункт меню")
                print("Выберите один из предложенных вариантов")
        print()
    return file_type


def load_data(file_type: FileType) -> LibraryHandler:
    match file_type:
        case FileType.TXT:
            data = read_txt_file()
            print("Данные загружены в систему")

        case FileType.JSON:
            data = read_json_file()
            print("Данные загружены в систему")

        case _:
            data = LibraryHandler()
            print("Ошибка! Данные не загружены")
    print()
    return data


def save_data(file_type: FileType, data):
    match file_type:
        case FileType.TXT:
            write_txt_file(data)
            print("Данные сохранены в текстовый файл")

        case FileType.JSON:
            write_json_file(data)
            print("Данные сохранены в json файл")

        case _:
            print("Ошибка! Данные НЕ сохранены")
    print()


# endregion

# region Convert
def __check_int(value) -> int | bool:
    try:
        value = int(value)
    except ValueError:
        print('Введите число!')
        return False
    return value


def __check_date(value) -> date | bool:
    try:
        value = text_to_date(value)
    except ValueError:
        print('Введите дату в формате год-месяц-день!')
        return False
    return value


def __input_int() -> int:
    is_processed = False
    while is_processed is False:
        option = input(">> ")
        option = __check_int(option)
        if option is not False:
            is_processed = True
    return option


def __input_date() -> date:
    is_processed = False
    while is_processed is False:
        option = input(">> ")
        option = __check_date(option)
        if option is not False:
            is_processed = True
    return option


# endregion


def books(data: LibraryHandler):
    is_processed = False
    while is_processed is False:
        print("--- Книги ---")
        print("Выберите действие")
        print("1 - Вывести на экран")
        print("2 - Добавить")
        print("3 - Редактировать")
        print("4 - Удалить")
        print("0 - Назад")
        option = input(">> ")
        match option:
            case "1":
                print(data.get_info_about_books())

            case "2":
                print("--- Новая книга ---")
                print("Введите идентификатор")
                option = __input_int()
                book = Book(option)

                print("Введите название")
                option = input(">> ")
                book.title = option

                print("Введите автора")
                option = input(">> ")
                book.author = option

                print("Введите жанр")
                option = input(">> ")
                book.genre = option

                print("Введите возрастной рейтинг")
                option = __input_int()
                book.age_mark = option

                print("Введите кол-во экземпляров")
                option = __input_int()
                book.count = option

                data.add_book(book)
                print('Книга добавлена')

                is_processed = False

            case "3":
                print("--- Редактирование информации о книге ---")
                print("Введите идентификатор")
                option = __input_int()
                if data.is_book_exists(option) is False:
                    print('Не найдена книга с указанным идентификатором')
                else:
                    id_book = option
                    book: Book
                    book = data.get_value_of_book_by_id(option)

                    while is_processed is False:
                        print("Выберите поле для редактирования")
                        print("1 - Название")
                        print("2 - Автор")
                        print("3 - Жанр")
                        print("4 - Возрастной рейтинг")
                        print("5 - Кол-во экземпляров")
                        print("6 - Сохранить изменения")
                        print("0 - Назад")
                        option = input(">> ")

                        match option:
                            case "1":
                                print("Введите название")
                                option = input(">> ")
                                book.title = option

                            case "2":
                                print("Введите автора")
                                option = input(">> ")
                                book.author = option

                            case "3":
                                print("Введите жанр")
                                option = input(">> ")
                                book.genre = option

                            case "4":
                                print("Введите возрастной рейтинг")
                                option = __input_int()
                                book.age_mark = option

                            case "5":
                                print("Введите кол-во экземпляров")
                                option = __input_int()
                                book.count = option

                            case "6":
                                data.edit_book(id_book, book)
                                print('Информация о книге отредактирована')
                                is_processed = True
                            case "0":
                                is_processed = True
                    is_processed = False

            case "4":
                while is_processed is False:
                    print("Введите идентификатор книги")
                    print("0 - Назад")
                    option = input(">> ")
                    match option:
                        case "0":
                            print()
                        case _:
                            try:
                                option = int(option)
                                if data.del_book(option) is True:
                                    print('Книга удалена')
                                    is_processed = True
                            except ValueError:
                                print('Введите число!')
                is_processed = False

            case "0":
                is_processed = True

            case _:
                print("Не найден указанный пункт меню")
                print("Выберите один из предложенных вариантов")
        print()


def readers(data):
    is_processed = False
    while is_processed is False:
        print("--- Читатели ---")
        print("Выберите действие")
        print("1 - Вывести на экран информацию о всех читателях")
        print("2 - Вывести на экран информацию о конкретном читателе")
        print("3 - Добавить")
        print("4 - Редактировать")
        print("5 - Удалить")
        print("0 - Назад")
        option = input(">> ")
        match option:
            case "1":
                print(data.get_info_about_readers())

            case "2":
                print(get_item_by_id(id_reader))
                print(data.get_info_about_books_of_reader(id_reader))

            case "3":
                print("--- Новый читатель ---")
                print("Введите номер читательского билета")
                option = __input_int()
                reader = Book(option)

                print("Введите ФИО")
                option = input(">> ")
                reader.fio = option

                print("Введите дату рождения")
                option = __input_date(">> ")
                reader.birthdate = option

                print("Введите телефон")
                option = input(">> ")
                reader.telephone = option

                data.add_reader(reader)
                print('Читатель добавлен')

                is_processed = False
            case "4":
                print("--- Редактирование информации о читателе ---")
                print("Введите читательского билета")
                option = __input_int()
                if data.is_reader_exists(option) is False:
                    print('Не найден читатель с указанным читательским билетом')
                else:
                    id_reader = option
                    reader: Reader
                    reader = data.get_value_of_reader_by_id(option)

                    while is_processed is False:
                        print("Выберите поле для редактирования")
                        print("1 - Название")
                        print("2 - ФИО")
                        print("3 - Дата рождения")
                        print("4 - Номер телефона")
                        print("5 - Добавить книгу")
                        print("6 - Удалить книгу")
                        print("7 - Сохранить изменения")
                        print("0 - Назад")
                        option = input(">> ")

                        match option:
                            case "1":
                                print("Введите название")
                                option = input(">> ")
                                reader.title = option

                            case "2":
                                print("Введите ФИО")
                                option = input(">> ")
                                reader.fio = option

                            case "3":
                                print("Введите дату рождения в формате год-месяц-день")
                                option = __input_date(">> ")
                                reader.birthdate = option

                            case "4":
                                print("Введите номер телефона")
                                option = input(">> ")
                                reader.telephone = option

                            case "5":
                                print("Введите ид книги")
                                option = __input_int()
                                if data.is_book_exists(option) is False:
                                    print("Книги с указанным ид не найдена в библиотеке")
                                elif data.readers.is_book_exists(option) is True:
                                    print("Книга с указанным ид уже взята читателем")
                                else:
                                    borrowed_book = BorrowedBook(option)
                                    print("Книга добавлена")

                                print("Введите дату взятия книги в формате год-месяц-день")
                                option = __input_date(">> ")
                                borrowed_book.date_borrowed = option

                                reader.add_book(borrowed_book)

                            case "6":
                                print("Введите ид книги")
                                print("0 - Назад")
                                option = input(">> ")
                                match option:
                                    case "0":
                                        print()
                                    case _:
                                        try:
                                            option = int(option)
                                            if reader.del_book(option) is True:
                                                print('Книга удалена')
                                                is_processed = True
                                        except ValueError:
                                            print('Введите число!')

                            case "7":
                                data.edit_book(id_reader, reader)
                                print('Информация о читателе отредактирована')
                                is_processed = True
                            case "0":
                                is_processed = True
                    is_processed = False
            case "5":
                while is_processed is False:
                    print("Введите идентификатор читателя")
                    print("0 - Назад")
                    option = input(">> ")
                    match option:
                        case "0":
                            print()
                        case _:
                            try:
                                option = int(option)
                                if data.del_reader(option) is True:
                                    print('Читатель удален')
                                    is_processed = True
                            except ValueError:
                                print('Введите число!')
                is_processed = False

            case "0":
                is_processed = True

            case _:
                print("Не найден указанный пункт меню")
                print("Выберите один из предложенных вариантов")
        print()


def choice_category(data):
    is_processed = False
    while is_processed is False:
        print("--- Выберите категорию ---")
        print("1 - Книги")
        print("2 - Читатели")
        print("0 - Выход")
        option = input(">> ")
        match option:
            case "1":
                books(data)
            case "2":
                readers(data)
            case "0":
                is_processed = True
            case _:
                print("Не найден указанный пункт меню")
                print("Выберите один из предложенных вариантов")
    print()


# region txt_file
def read_txt_file() -> LibraryHandler:
    """
    Чтение из текстового файла

    :return: данные по библиотеке
    """
    with open('data.txt', 'r') as f:
        text = f.read()
        data_for_file = read_library_from_string(text)
        f.close()
    return data_for_file


def write_txt_file(data_for_file: LibraryHandler):
    """
     Запись в текстовый файл

    :param data_for_file: данные по библиотеке
    """
    #
    with open('data.txt', 'w') as f:
        f.write(write_library_to_string(data_for_file))
        f.close()


# endregion

# region json
def read_json_file() -> LibraryHandler:
    """
    Чтение из json файла

    :return: данные по библиотеке
    """
    with codecs.open('data.json', 'r', encoding='utf-8') as f:
        text = f.read()
        data_for_file = json.loads(text, object_hook=library_hook_for_read_json)
    return data_for_file


def write_json_file(data_for_file):
    """
    Запись в json файл

    :param data_for_file: данные по библиотеке
    """

    # Параметры encoding='utf-8' и ensure_ascii=False нужны для подержки русского алфавита
    # Параметр indent=4 нужен для читабельности файла (уст. отступы в файле)
    # Параметр cls=CustomEncoder нужен для сериализации объекта пользовательского класса
    with codecs.open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data_for_file, f, ensure_ascii=False, indent=4, cls=CustomEncoder)


# endregion

def make_data() -> LibraryHandler:
    """
    Формирование стукрутры с данными по библиотеке

    :return: стукрутра с данными по библиотеке
    """
    books = [Book(1, "Диво Чудное. Том 1. Сказки Старой Руси", "Папсуев Роман Валентинович", "Фэнтези", 16, 2),
             Book(5, "Мифы Древней Греции", "Кун Николай Альбертович", "Фольклор", 6, 4),
             Book(2, "Безумная медицина", "Моррис Томас ", "Научно-популярная медицинская литература", 16, 1),
             Book(3, "Триумфальная арка", "Ремарк Эрих Мария ", "Роман", 16, 5)]

    first = Reader("789421454")
    first.fio = "Алёна Олеговна Берёзова"
    first.birthdate = date(2012, 2, 16)
    first.telephone = "89615556677"
    first.books = [BorrowedBook(books[1].id, date(2022, 6, 7), None, 14)]

    second = Reader("545678979", "Иван Васильевич Золотов", date(1999, 11, 25), "89612224457",
                    [BorrowedBook(books[1].id, date(2022, 8, 4), None, 14),
                     BorrowedBook(books[3].id, date(2022, 8, 7), None, 21)])
    third = Reader("147854547", "Ольга Александровна Романова", date(1986, 5, 18), "89619998547")
    return LibraryHandler(books, [first, second, third])
