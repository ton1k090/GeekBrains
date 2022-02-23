class ComplexNumber:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = "a + b * i"

    def __add__(self, other):
        print(f"Сумма x1 и x2 равна: ")
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        print("Произведение x1 и x2 равно: ")
        return ComplexNumber(self.x * other.x - self.y * other.y, self.y * other.x + self.x * other.y)

    def __str__(self):
        return f"z = {self.x} + {self.y} * i"

x_1 = ComplexNumber(0, -2)
x_2 = ComplexNumber(3, 4)
x_3 = x_1 + x_2
print(x_3)

x_4 = x_1 * x_2
print(x_4)