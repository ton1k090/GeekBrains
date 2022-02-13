class Clothes:

    def __init__(self, name):
        self.name = name


class Coat(Clothes):

    def __init__(self,size):
        super().__init__(size)
        self.size = float(size)

    def calc_coat(self):
        result = f"Суммарный расход ткани для {self.__class__.__name__}: {(self.size / 6.5 + 0.5)}"
        return result


class Suit(Clothes):
    def __init__(self,height):
        super().__init__(height)
        self.height = float(height)

    def calc_suit(self):
        result = f"Суммарный расход ткани для {self.__class__.__name__}: {(2 * self.height + 0.3)}"
        return result


coat = Coat(60)
print(coat.calc_coat())

suit = Suit(45)
print(suit.calc_suit())


