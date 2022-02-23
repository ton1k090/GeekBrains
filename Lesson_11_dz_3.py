class NotNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число для добавления в список: ')
        if value == 'stop'.lower().upper():
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Не поддерживаемый формат ввода данных!', ex)
print(my_list)