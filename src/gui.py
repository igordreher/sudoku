from tkinter import *
from sudoku import Sudoku


class App(Frame):
    def __init__(self, master=None, width='500', height='500'):
        super().__init__(master=master)
        self.master = master
        self.master.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self._init_canvas()

    def _init_canvas(self):
        self.canvas = Canvas(self)
        self._init_grid()
        self.canvas.pack(fill=BOTH, expand=1)

    def _init_grid(self):
        su = Sudoku()
        grid = su.grid
        size = 40

        for y in range(9):
            for x in range(9):
                if grid[y][x] != 0:
                    lb = Label(self.canvas, text=str(
                        grid[y][x]), relief=GROOVE)
                    lb.place(x=x*size, y=y*size, width=size, height=size)
                else:
                    e = Entry(self.canvas, justify=CENTER)
                    e.place(x=x*size, y=y*size, width=size, height=size)

    def say_hi(self):
        print("Hello World")


def main():
    root = Tk()
    app = App(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
