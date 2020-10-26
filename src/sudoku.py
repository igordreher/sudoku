import numpy as np
import random as rd


class Sudoku:

    EMPTY_CELL = 0

    def __init__(self):
        self._empty_grid()

    def __repr__(self):
        return str(np.array(self.grid))

    def create_puzzle(self, cells_to_clear=20):
        self._empty_grid()
        self.fill_grid()
        self._clear_cells(cells_to_clear)

    def _empty_grid(self):
        self.grid = []
        for _ in range(9):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def _copy_grid(grid):
        grid_copy = []
        for row in grid:
            grid_copy.append(row[:])

        return grid_copy

    def fill_grid(self):
        possible_values = list(range(1, 10))

        def loop():
            for y in range(9):
                for x in range(9):
                    if self.grid[y][x] == self.EMPTY_CELL:
                        rd.shuffle(possible_values)
                        for value in possible_values:
                            if self.is_value_possible(y, x, value):
                                self.grid[y][x] = value

                                if loop():
                                    return True

                                self.grid[y][x] = self.EMPTY_CELL
                        return False
            return True

        loop()

    def _clear_cells(self, cells_to_clear):
        while cells_to_clear > 0:
            y = rd.randint(0, 8)
            x = rd.randint(0, 8)
            if self.grid[y][x] != self.EMPTY_CELL:
                self.grid[y][x] = self.EMPTY_CELL
                cells_to_clear -= 1

    def is_value_possible(self, cell_y, cell_x, cell_value):
        for x in range(9):
            if self.grid[cell_y][x] == cell_value:
                return False
        for y in range(9):
            if self.grid[y][cell_x] == cell_value:
                return False

        cell_x_sqr = (cell_x//3)*3
        cell_y_sqr = (cell_y//3)*3

        for y in range(0, 3):
            for x in range(0, 3):
                if self.grid[cell_y_sqr+y][cell_x_sqr+x] == cell_value:
                    return False
        return True
