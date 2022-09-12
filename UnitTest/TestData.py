import unittest
from datetime import date, datetime, timedelta

from Data.Book import Book
from Data.BorrowedBook import BorrowedBook
from Data.Reader import Reader


class TestBook(unittest.TestCase):
    def setUp(self):
        self.A = Book(1)
        self.B = Book(4, "Большая книга славянских мифов", "Иликаев А.", "Антропология. Этнография", 6, 2)
        self.C: Book

    def test_init(self):
        self.assertEqual((self.A.id, self.A.title, self.A.author, self.A.genre, self.A.age_mark, self.A.count),
                         (1, "", "", "", 0, 0),
                         "Неверная инициализация объекта")

        self.assertEqual((self.B.id, self.B.title, self.B.author, self.B.genre, self.B.age_mark, self.B.count),
                         (4, "Большая книга славянских мифов", "Иликаев А.", "Антропология. Этнография", 6, 2),
                         "Неверная инициализация объекта")

    def test_copy(self):
        self.C = self.B.copy()

        self.assertIsNot(self.B, self.C, "Неверное копирование объекта")
        self.assertEqual((self.B.id, self.B.title, self.B.author, self.B.genre, self.B.age_mark, self.B.count),
                         (self.C.id, self.C.title, self.C.author, self.C.genre, self.C.age_mark, self.C.count),
                         "Неверное копирование объекта")

        self.C.title = "Юлий Цезарь. В походах и битвах"
        self.C.author = "Голицын Н.С."
        self.C.genre = "История войн"
        self.C.age_mark = 16
        self.C.count = 8
        self.assertEqual((4, "Юлий Цезарь. В походах и битвах", "Голицын Н.С.", "История войн", 16, 8),
                         (self.C.id, self.C.title, self.C.author, self.C.genre, self.C.age_mark, self.C.count),
                         "Неверное копирование объекта")

        self.assertNotEqual((self.B.id, self.B.title, self.B.author, self.B.genre, self.B.age_mark, self.B.count),
                            (self.C.id, self.C.title, self.C.author, self.C.genre, self.C.age_mark, self.C.count),
                            "Неверное копирование объекта")

    @staticmethod
    def main():
        unittest.main()


class TestBorrowedBook(unittest.TestCase):
    def setUp(self):
        self.A = BorrowedBook(1)
        self.B = BorrowedBook(2, date(2022, 11, 14), date(2010, 12, 7))
        self.C = BorrowedBook(3, date(2022, 8, 8), None, 18)
        self.D = BorrowedBook(4, date(2022, 9, 18))

    def test_init(self):
        self.assertEqual((self.A.id, self.A.date_borrowed, self.A.date_will_return),
                         (1, datetime.today().date(), datetime.today().date() + timedelta(days=14)),
                         "Неверная инициализация объекта")

        self.assertEqual((self.B.id, self.B.date_borrowed, self.B.date_will_return),
                         (2, date(2022, 11, 14), date(2010, 12, 7)),
                         "Неверная инициализация объекта")

        self.assertEqual((self.C.id, self.C.date_borrowed, self.C.date_will_return),
                         (3, date(2022, 8, 8), date(2022, 8, 8) + timedelta(days=18)),
                         "Неверная инициализация объекта")

        self.assertEqual((self.D.id, self.D.date_borrowed, self.D.date_will_return),
                         (4, date(2022, 9, 18), date(2022, 9, 18) + timedelta(days=14)),
                         "Неверная инициализация объекта")

    @staticmethod
    def main():
        unittest.main()


class TestReader(unittest.TestCase):
    def setUp(self):
        books = [BorrowedBook(1),
                 BorrowedBook(2, date(2022, 11, 14), date(2010, 12, 7)),
                 BorrowedBook(3, date(2022, 8, 8), None, 18),
                 BorrowedBook(4, date(2022, 9, 18))]
        self.A = Reader(1)
        self.B = Reader(4, "Марсов Анатолий Вячеславович", date(2000, 1, 21), "89612223344", books)
        self.C: Reader
        self.D = Reader(11, "Кольцов Виктор Иванович", date(1988, 6, 4), "89618889977")

    def test_init(self):
        self.assertEqual((self.A.id, self.A.fio, self.A.birthdate, self.A.telephone, self.A.books),
                         ("1", "", date(1900, 1, 1), "", []),
                         "Неверная инициализация объекта")

        self.assertEqual((self.B.id, self.B.fio, self.B.birthdate, self.B.telephone, self.B.books),
                         ("4", "Марсов Анатолий Вячеславович", date(2000, 1, 21), "89612223344", self.B.books),
                         "Неверная инициализация объекта")

    def test_copy(self):
        self.C = self.B.copy()

        self.assertIsNot(self.B, self.C, "Неверное копирование объекта")
        self.assertEqual((self.B.id, self.B.fio, self.B.birthdate, self.B.telephone),
                         (self.C.id, self.C.fio, self.C.birthdate, self.C.telephone),
                         "Неверное копирование объекта")

        self.C.fio = "Волков Никита Арсеньевич"
        self.C.birthdate = date(1999, 1, 1)
        self.C.telephone = "89615554477"
        self.assertEqual(("4", "Волков Никита Арсеньевич", date(1999, 1, 1), "89615554477"),
                         (self.C.id, self.C.fio, self.C.birthdate, self.C.telephone),
                         "Неверное копирование объекта")

        self.assertNotEqual((self.B.id, self.B.fio, self.B.birthdate, self.B.telephone, self.B.books),
                            (self.C.id, self.C.fio, self.C.birthdate, self.C.telephone, self.C.books),
                            "Неверное копирование объекта")

    @staticmethod
    def main():
        unittest.main()


# Executing the tests in the above test case class
if __name__ == '__main__':
    unittest.main()
