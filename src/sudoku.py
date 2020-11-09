import numpy
import random


class Sudoku:

    EMPTY_CELL = 0

    def __init__(self):
        self._clear_grid()

    def __repr__(self):
        return str(numpy.array(self.grid))

    def generate_new_puzzle(self, n_of_blank_cells=20):
        self._clear_grid()
        self.fill_grid()
        self._clear_random_cells(n_of_blank_cells)

    def _clear_grid(self):
        self.grid = []
        for _ in range(9):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    def fill_grid(self):
        possible_values = list(range(1, 10))

        def loop():
            for y in range(9):
                for x in range(9):
                    if self.grid[y][x] == self.EMPTY_CELL:
                        random.shuffle(possible_values)
                        cell_position = (x, y)
                        for value in possible_values:

                            if self.is_value_possible(value, cell_position):
                                self.grid[y][x] = value

                                if loop():
                                    return True

                                self.grid[y][x] = self.EMPTY_CELL
                        return False
            return True

        loop()

    def is_value_possible(self, value, cell_position):
        cell_x, cell_y = cell_position

        if self._is_value_in_row(value, cell_y):
            return False

        if self._is_value_in_column(value, cell_x):
            return False

        if self._is_value_in_cell_box(value, cell_position):
            return False

        return True

    def _is_value_in_row(self, value, row):
        if value in self.grid[row]:
            return True
        return False

    def _is_value_in_column(self, value, column):
        rows = range(9)
        for row in rows:
            if self.grid[row][column] == value:
                return True
        return False

    def _is_value_in_cell_box(self, value, cell_position):
        cell_x, cell_y = cell_position
        box_x = (cell_x//3)*3
        box_y = (cell_y//3)*3

        for y in range(3):
            for x in range(3):
                if self.grid[box_y+y][box_x+x] == value:
                    return True
        return False

    def _clear_random_cells(self, number_of_cells):
        while number_of_cells > 0:
            y = random.randint(0, 8)
            x = random.randint(0, 8)
            if self.grid[y][x] != self.EMPTY_CELL:
                self.grid[y][x] = self.EMPTY_CELL
                number_of_cells -= 1
