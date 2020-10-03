from tkinter import *
from sudoku import Sudoku


class App(Frame):
    def __init__(self, master=None, cell_size=int(40)):
        super().__init__(master=master, width=cell_size*9+3*2, height=cell_size*9+3*2)
        self.master = master
        self.master.title("Sudoku")
        self.cell_size = cell_size
        self.size = self.cell_size*9+3*2
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
        self.canvas = Canvas(self, width=self.size,
                             height=self.size, bg='black')
        self._init_grid()
        self.canvas.pack()

    def _init_grid(self):
        su = Sudoku()
        grid = su.grid
        size = self.cell_size
        gap = 3
        vcmd = (self.register(self._only_int))

        for y in range(9):
            if (y//3)*3 == 0:
                ygap = gap*0
            elif (y//3)*3 == 3:
                ygap = gap*1
            else:
                ygap = gap*2

            for x in range(9):
                if (x//3)*3 == 0:
                    xgap = gap*0
                elif (x//3)*3 == 3:
                    xgap = gap*1
                else:
                    xgap = gap*2

                if grid[y][x] != 0:
                    lb = Label(self.canvas, text=str(
                        grid[y][x]), bg='white', fg='black', relief=SUNKEN, font='10')
                    lb.place(x=x*size+xgap, y=y*size +
                             ygap, width=size, height=size)

                else:
                    e = Entry(self.canvas, justify=CENTER, bg='white', fg='black', font='10',
                              bd=1, highlightcolor='red', highlightthickness=0, insertbackground='gray', validate='key', vcmd=(vcmd, '%P'))
                    e.place(x=x*size+xgap, y=y*size +
                            ygap, width=size, height=size)
                    e.bind('<FocusIn>', self._on_focus)
                    e.bind('<FocusOut>', self._off_focus)

    def _on_focus(self, evt):
        evt.widget.config(bg='gray')

    def _off_focus(self, evt):
        evt.widget.config(bg='white')

    def _only_int(self, P):
        if P:
            if not P.isdigit():
                return False
            if len(P) > 1:
                return False
        return True


def main():
    root = Tk()
    app = App(root)
    app.mainloop()


if __name__ == "__main__":
    main()
