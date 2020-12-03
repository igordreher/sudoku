"""Sudoku puzzle generator/solver"""

from __future__ import annotations
from typing import List, Tuple
import random
import numpy


class Sudoku:
    """Handles a Sudoku puzzle"""

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
        cell_pairs_to_clear = (81-n_of_hints) / 2
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
                    cell = Cell(self.grid, (x, y))
                    return self._is_solution_possible(cell)
        return True

    def _is_solution_possible(self, cell: Cell):
        possible_values = list(range(1, 10))
        cell_x, cell_y = cell.get_position()
        random.shuffle(possible_values)

        for value in possible_values:
            if cell.is_value_possible(value):
                self.grid[cell_y][cell_x] = value

                is_grid_filled = self.fill_grid()
                if is_grid_filled:
                    return True
                self.grid[cell_y][cell_x] = self.EMPTY_CELL

        return False

    def _clear_random_cell_pairs(self, number_of_pairs):
        while number_of_pairs > 0:
            cell_x = random.randint(0, 8)
            cell_y = random.randint(0, 8)
            if self.grid[cell_y][cell_x] != self.EMPTY_CELL:
                self._clear_cell_pair((cell_x, cell_y))
                number_of_pairs -= 1

    def _clear_cell_pair(self, first_cell_position):
        cell_x, cell_y = first_cell_position
        opposite_y = 8 - cell_y
        opposite_x = 8 - cell_x
        self.grid[cell_y][cell_x] = self.EMPTY_CELL
        self.grid[opposite_y][opposite_x] = self.EMPTY_CELL


class Cell:
    """Handles cell possibility"""

    def __init__(self, grid: List[list], position=(0, 0)) -> None:
        self.grid = grid
        self.position = position
        self.value = 0

    def get_position(self) -> Tuple[int, int]:
        return self.position

    def is_value_possible(self, value) -> bool:
        """
        Checks if given value is possible
        """
        self.value = value

        if self._is_value_in_row():
            return False

        if self._is_value_in_column():
            return False

        if self._is_value_in_box():
            return False

        return True

    def _is_value_in_row(self):
        row = self.position[1]

        if self.value in self.grid[row]:
            return True
        return False

    def _is_value_in_column(self):
        column = self.position[0]
        rows = range(9)

        for row in rows:
            if self.grid[row][column] == self.value:
                return True
        return False

    def _is_value_in_box(self):
        cell_x, cell_y = self.position
        box_x = (cell_x//3) * 3
        box_y = (cell_y//3) * 3

        for y in range(3):
            for x in range(3):
                if self.grid[box_y + y][box_x + x] == self.value:
                    return True
        return False
