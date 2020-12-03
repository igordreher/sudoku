import unittest
from src.sudoku import Sudoku, Cell

EXAMPLE_GRID = [[1, 3, 9, 8, 7, 6, 2, 5, 4], [6, 2, 5, 1, 9, 4, 7, 3, 8],
                [7, 4, 8, 2, 5, 3, 1, 6, 9], [8, 6, 7, 4, 2, 5, 3, 9, 1],
                [4, 9, 1, 3, 6, 7, 5, 8, 2], [3, 5, 2, 9, 8, 1, 6, 4, 7],
                [5, 1, 6, 7, 4, 8, 9, 2, 3], [9, 7, 4, 6, 3, 2, 8, 1, 5],
                [2, 8, 3, 5, 1, 9, 4, 7, 6]]


class TestSudoku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sudoku = Sudoku()

    def setUp(self):
        grid_copy = []
        for row in EXAMPLE_GRID:
            grid_copy.append(row[:])
        self.sudoku.grid = grid_copy

    def test_grid_is_empty(self):
        self.sudoku.clear_grid()

        for y in range(9):
            for x in range(9):
                assert self.sudoku.grid[y][x] == 0

    def test_grid_rows_not_copy(self):
        self.sudoku.clear_grid()

        for y in range(9):
            assert self.sudoku.grid[y] is not self.sudoku.grid[y - 1]

    def test_grid_filled(self):
        self.sudoku.clear_grid()
        self.sudoku.fill_grid()

        for y in range(9):
            for x in range(9):
                assert self.sudoku.grid[y][x] != 0

    def test_grid_filled_all_possible(self):
        self.sudoku.clear_grid()
        self.sudoku.fill_grid()

        for y in range(9):
            for x in range(9):
                cell = Cell(self.sudoku.grid, (x, y))
                number = cell.grid[y][x]
                cell.grid[y][x] = 0

                assert cell.is_value_possible(number)

    def test_number_of_cleared_cells(self):
        self.sudoku._clear_random_cell_pairs(15)
        count = 0

        for y in range(9):
            for x in range(9):
                if self.sudoku.grid[y][x] == 0:
                    count += 1

        assert count is 30 or count is 29


class TestCellPossibility(unittest.TestCase):

    def setUp(self) -> None:
        grid_copy = []
        for row in EXAMPLE_GRID:
            grid_copy.append(row[:])

        self.cell = Cell(grid_copy)

    def test_values_in_row(self):
        for number in range(1, 10):
            self.cell.value = number
            assert self.cell._is_value_in_row()

    def test_values_not_in_row(self):
        self.cell.grid[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for number in range(1, 10):
            self.cell.value = number
            assert not self.cell._is_value_in_row()

    def test_values_in_column(self):
        for number in range(1, 10):
            self.cell.value = number
            assert self.cell._is_value_in_column()

    def test_values_not_in_column(self):
        for row in self.cell.grid:
            row[0] = 0

        for number in range(1, 10):
            self.cell.value = number
            assert not self.cell._is_value_in_column()

    def test_value_in_cell_box(self):

        for number in range(1, 10):
            self.cell.value = number
            assert self.cell._is_value_in_box()

    def test_values_not_in_cell_box(self):
        for y in range(3):
            for x in range(3):
                self.cell.value = self.cell.grid[y][x]
                self.cell.grid[y][x] = 0
                assert not self.cell._is_value_in_box()

    def test_value_is_not_possible(self):
        for number in range(1, 10):
            assert not self.cell.is_value_possible(number)

    def test_all_values_possible(self):
        for y in range(9):
            for x in range(9):
                self.cell.position = (x, y)
                value = self.cell.grid[y][x]
                self.cell.grid[y][x] = 0
                assert self.cell.is_value_possible(value)
                self.cell.grid[y][x] = self.cell.value
