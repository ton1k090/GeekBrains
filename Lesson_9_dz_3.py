class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        data = f"Имя: {self.name}, Фамилия: {self.surname}"
        return data

    def get_total_income(self):
        income = f"Доход с учётом премии {self.name}, состовляет: {sum(self._income.values())}"
        return income


employee = Position("Анастасия", "Троянова", "Директор", 75000, 5000)
print(employee.get_full_name())
print(employee.get_total_income())