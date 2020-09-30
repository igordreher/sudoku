import numpy as np
import random as rd


class Sudoku:

    def __init__(self):
        self.grid = self.mk_grid()
        self.gen_puzzle()

    def __repr__(self):
        return str(np.array(self.grid))

    @staticmethod
    def mk_grid(grid=None):
        new_grid = []
        if not grid:
            for _ in range(9):
                new_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        else:
            for row in grid:
                new_grid.append(row[:])
        return new_grid

    def fill_grid(self, random=True, solve=True):
        lst = list(range(1, 10))
        if solve:
            grid = self.grid
        else:
            grid = self.mk_grid(self.grid)

        def loop(random, solve):
            for y in range(9):
                for x in range(9):
                    if grid[y][x] == 0:
                        if random:
                            rd.shuffle(lst)
                        for n in lst:
                            if self.possible(y, x, n):
                                grid[y][x] = n

                                if loop(random, solve):
                                    return True

                                grid[y][x] = 0
                        return False
            return True

        return loop(random, solve)

    def gen_puzzle(self, clears=20):
        self.grid = self.mk_grid()
        self.fill_grid()

        def loop():
            nonlocal clears
            while clears > 0:
                y = rd.randint(0, 8)
                x = rd.randint(0, 8)
                if self.grid[y][x] != 0:
                    n = self.grid[y][x]
                    self.grid[y][x] = 0
                    clears -= 1
                    if self.fill_grid(False, False):
                        loop()
                    else:
                        self.grid[y][x] = n
                        clears += 1
        loop()

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
