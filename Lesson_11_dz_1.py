class Date:
    def __init__(self, date_format):
        self.date_format = date_format

    @classmethod
    def date_formatting(cls, self):
        day, month, year = self.date_format.split("-")
        return int(day), int(month), int(year)

    @staticmethod
    def date_validation(date):
        day, month, year = date
        try:
            if not 1 <= day <= 31:
                print("Допустимы значения дня от 1 до 31")
            if not month <= 12:
                print("Допустимые значения месяца от 1 до 12")
            if not len(str(year)) == 4:
                print("Значение года имеет 4 разряда")
        except AssertionError as err:
            return print(err)


a = Date("32-1-11435")
print(Date.date_formatting(a))
Date.date_validation(Date.date_formatting(a))
