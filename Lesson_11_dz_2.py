import random


class Exceptions(BaseException):
    pass


random_number = random.randrange(1, 10000)
divider = int(input("Введите число: "))

try:
    if divider == 0:
        raise Exceptions("Ошибка! Введите любое число кроме нуля!")
except ZeroDivisionError as err:
    print(err)
else:
    result = random_number // divider
    print(f"Выпало число с номером {result}")