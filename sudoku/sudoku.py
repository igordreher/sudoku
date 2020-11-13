import random
from typing import Tuple
import numpy


class Sudoku:

    EMPTY_CELL = 0

    def __init__(self):
        """Start grid as an empty list[9][9]"""
        self.clear_grid()

    def __repr__(self):
        return str(numpy.array(self.grid))

    def generate_new_puzzle(self, n_of_hints: int):
        """
        Clears grid and generates a new puzzle with, closely, given number of hints
        """
        cell_pairs_to_clear = (81-n_of_hints)/2
        self.clear_grid()
        self.fill_grid()
        self._clear_random_cell_pairs(cell_pairs_to_clear)

    def clear_grid(self):
        """Empty all cells"""
        self.grid = []
        for _ in range(9):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    def fill_grid(self):
        """Solves the puzzle, filling the grid"""
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == self.EMPTY_CELL:
                    cell_position = (x, y)
                    return self._is_solution_possible(cell_position)
        return True

    def _is_solution_possible(self, cell_position):
        possible_values = list(range(1, 10))
        x, y = cell_position
        random.shuffle(possible_values)
        for value in possible_values:
            if self.is_value_possible(value, cell_position):
                self.grid[y][x] = value

                is_grid_filled = self.fill_grid()
                if is_grid_filled:
                    return True

                self.grid[y][x] = self.EMPTY_CELL
        return False

    def is_value_possible(self, value: int, cell_position: Tuple[int, int]) -> bool:
        """
        Checks if value is possible on given position
        """
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

    def _clear_random_cell_pairs(self, number_of_pairs):
        while number_of_pairs > 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if self.grid[y][x] != self.EMPTY_CELL:
                self._clear_cell_pair((x, y))
                number_of_pairs -= 1

    def _clear_cell_pair(self, first_cell_position):
        x, y = first_cell_position
        opposite_y = 8-y
        opposite_x = 8-x
        self.grid[y][x] = self.EMPTY_CELL
        self.grid[opposite_y][opposite_x] = self.EMPTY_CELL
