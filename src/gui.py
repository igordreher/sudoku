from tkinter import *
from functools import partial
from sudoku import Sudoku


class App(Frame):
    def __init__(self, master=None, cell_size=int(50)):
        super().__init__(master=master)
        self.master = master
        self.master.title("Sudoku")
        self.puzzle = Sudoku()
        self.cell_size = cell_size
        self.size = self.cell_size*9+3*2
        self._init_canvas()
        self.menu()
        self.center()
        self.pack(fill=BOTH, expand=1)

    def menu(self):
        menubar = Menu(self)
        new_game = Menu(menubar, tearoff=0)
        new_game.add_command(label='Easy', command=partial(self.new_puzzle, dif='easy'))
        new_game.add_command(label='Normal', command=partial(self.new_puzzle, dif='normal'))
        new_game.add_command(label='Hard', command=partial(self.new_puzzle, dif='hard'))
        menubar.add_cascade(label='New Game', menu=new_game)
        self.master.config(menu=menubar)

    def new_puzzle(self, dif='normal', hints=0):
        if dif == 'normal':
            self.puzzle.gen_puzzle(81-40)
        elif dif == 'easy':
            self.puzzle.gen_puzzle(81-60)
        elif dif == 'hard':
            self.puzzle.gen_puzzle(81-26)
        else:
            self.puzzle.gen_puzzle(81-int(hints))

        self._init_grid()

    def center(self):
        root = self.master
        screen_w = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        x = int(screen_w/2 - self.size/2)
        y = int(screen_y/2 - self.size/2)
        root.geometry("+{}+{}".format(x, y))
        self.update()
        root.minsize(self.size, self.size)

    def _init_canvas(self):
        self.canvas = Canvas(self, bg='black')
        self.new_puzzle()
        self.canvas.pack(fill=BOTH, expand=1)

    def _init_grid(self):
        grid = self.puzzle.grid
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
                        grid[y][x]), bg='white', fg='black', relief=SUNKEN, font='11')
                    lb.place(x=x*size+xgap, y=y*size +
                             ygap, width=size, height=size)

                else:
                    e = Entry(self.canvas, justify=CENTER, bg='#dddddd', fg='black', font='11',
                              bd=1, highlightcolor='red', highlightthickness=0, insertbackground='black', validate='key', vcmd=(vcmd, '%P'))
                    e.place(x=x*size+xgap, y=y*size +
                            ygap, width=size, height=size)
                    e.x = x
                    e.y = y
                    e.bind('<Return>', self._on_enter)
                    e.bind('<BackSpace>', self._on_delete)

    def _on_enter(self, evt):
        x = evt.widget.x
        y = evt.widget.y
        value = int(evt.widget.get())
        if self.puzzle.possible(y, x, value):
            evt.widget.config(fg='green')
        else:
            evt.widget.config(fg='red')
        self.puzzle.grid[y][x] = value

    def _on_delete(self, evt):
        x = evt.widget.x
        y = evt.widget.y
        self.puzzle.grid[y][x] = 0
        evt.widget.config(fg='black')

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
