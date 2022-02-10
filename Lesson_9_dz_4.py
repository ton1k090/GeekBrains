class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Полицейский автомобиль {self.name} начал движение со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"{self.name} Останавливается")

    def on_turn(self):
        print(f"{self.name} дижется прямо")

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль Марки {self.name}, немедленно остановитесь")
        else:
            print(f"Скорость {self.name}, {self.speed}")


class SportCar(Car):

    def show_speed(self):
        print(f"Автомобиль {self.name}, движется со скоростью {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль Марки {self.name}, немедленно остановитесь")
        else:
            print(f"Скорость {self.name}, {self.speed}")


class PoliceCar(Car):
    def show_speed(self):
        print(f"Полицейский автомобиль, движется со скоростью {self.speed}")


car_1 = Car(90, "Синий", "Lancer")
car_1.go()
car_2 = TownCar(80, "Красный", "Москвич")
car_2.show_speed()
car_3 = WorkCar(40, "Чёрный", "MAN")
car_3.show_speed()
