class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_of_mass(self, weight=31, thickness=45):
        result = (self._length * self._width * weight * thickness // 1000)
        return result


a = Road(20, 500)
print(a.calculation_of_mass())

