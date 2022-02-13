class Cell:
    def __init__(self, qty_cells):
        self.qty_cells = int(qty_cells)
        self.qty_cells = qty_cells

    def __add__(self, other):
        print("Сумма клеток ")
        return Cell(self.qty_cells + other.qty_cells)

    def __sub__(self, other):
        print("Вычитание ячейки: ")
        if self.qty_cells - other.qty_cells > 0:
            return Cell(self.qty_cells - other.qty_cells)
        else:
            return print("Разность равна 0")

    def __mul__(self, other):
        print("Умножение ячейки: ")
        return Cell(self.qty_cells * other.qty_cells)

    def __truediv__(self, other):
        print("Деление ячейки")
        return Cell(self.qty_cells // other.qty_cells)

    def make_order(self, rows_of_cells):
        rows = ["*" * rows_of_cells] * self.qty_cells
        return "\n".join(rows)


cell1 = Cell(12)
cell2 = Cell(5)
cell3 = cell1 - cell2
print(cell3.qty_cells)

cell3.make_order(2)
print(cell3.make_order(3))
