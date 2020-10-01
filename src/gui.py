from tkinter import *
from sudoku import Sudoku


class App(Frame):
    def __init__(self, master=None, cell_size=int(40)):
        super().__init__(master=master, width=cell_size*9, height=cell_size*9)
        self.master = master
        self.master.title("Sudoku")
        self.cell_size = cell_size
        self.size = self.cell_size*9
        self._init_canvas()
        self.center()
        self.pack()

    def center(self):
        root = self.master
        screen_w = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        x = int(screen_w/2 - self.winfo_reqwidth()/2)
        y = int(screen_y/2 - self.winfo_reqheight()/2) 
        root.geometry("+{}+{}".format(x, y))
        self.update()
        root.minsize(self.winfo_reqwidth(), self.winfo_reqheight())
        root.maxsize(self.winfo_reqwidth(), self.winfo_reqheight())

    def _init_canvas(self):
        self.canvas = Canvas(self, width=self.size, height=self.size)
        self._init_grid()
        self.canvas.pack()

    def _init_grid(self):
        su = Sudoku()
        grid = su.grid
        size = self.cell_size

        for y in range(9):
            for x in range(9):
                if grid[y][x] != 0:
                    lb = Label(self.canvas, text=str(
                        grid[y][x]), relief=GROOVE)
                    lb.place(x=x*size, y=y*size, width=size, height=size)
                else:
                    e = Entry(self.canvas, justify=CENTER)
                    e.place(x=x*size, y=y*size, width=size, height=size)


def main():
    root = Tk()
    app = App(root)
    app.mainloop()


if __name__ == "__main__":
    main()
