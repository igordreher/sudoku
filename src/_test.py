import unittest
from src.sudoku import Sudoku


class TestSudoku(unittest.TestCase):

    EXAMPLE_GRID = [[1, 3, 9, 8, 7, 6, 2, 5, 4],
                    [6, 2, 5, 1, 9, 4, 7, 3, 8],
                    [7, 4, 8, 2, 5, 3, 1, 6, 9],
                    [8, 6, 7, 4, 2, 5, 3, 9, 1],
                    [4, 9, 1, 3, 6, 7, 5, 8, 2],
                    [3, 5, 2, 9, 8, 1, 6, 4, 7],
                    [5, 1, 6, 7, 4, 8, 9, 2, 3],
                    [9, 7, 4, 6, 3, 2, 8, 1, 5],
                    [2, 8, 3, 5, 1, 9, 4, 7, 6]]

    @classmethod
    def setUpClass(cls):
        cls.sudoku = Sudoku()

    def setUp(self):
        grid_copy = []
        for row in self.EXAMPLE_GRID:
            grid_copy.append(row[:])
        self.sudoku.grid = grid_copy

    def test_grid_is_empty(self):
        self.sudoku.clear_grid()
        grid = self.sudoku.grid

        for y in range(9):
            assert grid[y] is not grid[y-1]
            for x in range(9):
                assert grid[y][x] == 0

    def test_value_in_row(self):
        for number in range(1, 10):
            assert self.sudoku._is_value_in_row(number, 0)

        self.sudoku.grid[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for number in range(1, 10):
            assert not self.sudoku._is_value_in_row(number, 0)

    def test_value_in_column(self):
        for number in range(1, 10):
            assert self.sudoku._is_value_in_column(number, 0)
        for row in self.sudoku.grid:
            number = row[0]
            row[0] = 0
            assert not self.sudoku._is_value_in_column(number, 0)

    def test_value_in_cell_box(self):
        for number in range(1, 10):
            assert self.sudoku._is_value_in_cell_box(number, (0, 0))

        for y in range(3):
            for x in range(3):
                number = self.sudoku.grid[y][x]
                self.sudoku.grid[y][x] = 0
                assert not self.sudoku._is_value_in_cell_box(number, (0, 0))

    def test_value_is_not_possible(self):
        for number in range(1, 10):
            assert not self.sudoku.is_value_possible(number, (0, 0))

    def test_all_values_possible(self):

        for y in range(9):
            for x in range(9):
                number = self.sudoku.grid[y][x]
                assert not self.sudoku.is_value_possible(number, (x, y))
                self.sudoku.grid[y][x] = 0
                assert self.sudoku.is_value_possible(number, (x, y))
                self.sudoku.grid[y][x] = number

    def test_grid_filled(self):
        self.sudoku.clear_grid()
        self.sudoku.fill_grid()
        print(self.sudoku)

        for y in range(9):
            for x in range(9):
                assert self.sudoku.grid[y][x] != 0

    def test_grid_filled_all_possible(self):
        self.sudoku.clear_grid()
        self.sudoku.fill_grid()

        for y in range(9):
            for x in range(9):
                number = self.sudoku.grid[y][x]
                assert not self.sudoku.is_value_possible(number, (x, y))
                self.sudoku.grid[y][x] = 0
                assert self.sudoku.is_value_possible(number, (x, y))
                self.sudoku.grid[y][x] = number

    def test_number_of_cleared_cells(self):
        self.sudoku._clear_random_cell_pairs(15)
        count = 0

        for y in range(9):
            for x in range(9):
                if self.sudoku.grid[y][x] == 0:
                    count += 1

        assert count is 30 or count is 29
