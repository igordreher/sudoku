import numpy as np
import random as rd


class Sudoku:

    def __init__(self):
        self.grid = self.mk_grid()

    def __repr__(self):
        return str(np.array(self.grid))

    @staticmethod
    def mk_grid():
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        return grid

    def gen_grid(self):
        lst = list(range(1, 10))
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    rd.shuffle(lst)
                    for n in lst:
                        if self.possible(y, x, n):
                            self.grid[y][x] = n
                            if self.gen_grid():
                                return True
                            self.grid[y][x] = 0
                    return False
        return True

    def possible(self, y, x, n):
        for i in range(9):
            if self.grid[y][i] == n:
                return False
        for i in range(9):
            if self.grid[i][x] == n:
                return False

        x_sqr = (x//3)*3
        y_sqr = (y//3)*3

        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y_sqr+i][x_sqr+j] == n:
                    return False
        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
        print(np.matrix(self.grid))
        input("Next?")
