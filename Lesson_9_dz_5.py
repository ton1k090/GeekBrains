class Stationery:
    def __init__(self, title="канцелярская_принадлежность"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} Ручка")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} Карандаш")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} Маркер")


a = Pen()
a.draw()

b = Pencil()
b.draw()

c = Handle()
c.draw()
