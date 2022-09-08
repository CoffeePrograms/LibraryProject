from datetime import date, datetime, timedelta


# todo write and read for file
class BorrowedBook:
    """ Книга, одолженная читателем """
    # region Fields
    __id: int
    __date_borrowed: date
    __date_will_return: date

    # endregion

    def __init__(self, id_book, date_borrowed=datetime.today().date(), date_will_return=None, days_for_borrow=14):
        self.__id = int(id_book)
        self.__date_borrowed = date_borrowed
        if date_will_return is None:
            self.__date_will_return = date_borrowed + timedelta(days=days_for_borrow)
        else:
            self.__date_will_return = date_will_return

    # region Properties
    @property
    def id(self):
        """ Идентификатор """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = int(value)

    @property
    def date_borrowed(self):
        """ Дата взятия книги """
        return self.__date_borrowed

    @date_borrowed.setter
    def date_borrowed(self, value):
        self.__date_borrowed = value

    @property
    def date_will_return(self):
        """ Предполагаемая дата возврата книги """
        return self.__date_will_return

    @date_will_return.setter
    def date_will_return(self, value):
        self.__date_will_return = value

    @property
    def overdue_days(self):
        """ Задолженность в днях """
        days = int((datetime.now().date() - self.__date_will_return).days)
        return days if days > 0 else 0

    @property
    def is_overdue(self):
        """ Есть ли задолженность по книге """
        return self.overdue_days > 0

    # endregion

    # region Methods
    def prolong(self, days_prolong):
        """ Продление """
        return self.__date_will_return + timedelta(days=days_prolong)

    def __str__(self):
        return f"Книга №: {self.__id}\nДата выдачи: {self.date_borrowed}\n" \
               f"Предполагаемая дата возврата: {self.date_will_return}\n"
    # endregion
