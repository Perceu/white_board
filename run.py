from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):

    PEN_SIZE = 2.0
    ERASER_SIZE = 20.0
    DEFAULT_BLACK = 'black'
    DEFAULT_RED = 'red'
    DEFAULT_BLUE = 'blue'
    DEFAULT_GREEN = 'green'

    def __init__(self):
        self.root = Tk()

        self.pen_button_black = Button(self.root, text='B', bg=self.DEFAULT_BLACK, fg=self.DEFAULT_BLACK, command=self.use_pen_black)
        self.pen_button_black.grid(row=0, column=0)

        self.pen_button_red = Button(self.root, text='R', bg=self.DEFAULT_RED, fg=self.DEFAULT_RED, command=self.use_pen_red)
        self.pen_button_red.grid(row=0, column=1)

        self.pen_button_blue = Button(self.root, text='B', bg=self.DEFAULT_BLUE, fg=self.DEFAULT_BLUE, command=self.use_pen_blue)
        self.pen_button_blue.grid(row=0, column=2)

        self.pen_button_green = Button(self.root, text='G', bg=self.DEFAULT_GREEN, fg=self.DEFAULT_GREEN, command=self.use_pen_green)
        self.pen_button_green.grid(row=0, column=3)

        self.eraser_button = Button(self.root, text='apagador', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=4)

        self.clean_button = Button(self.root, text='limpar', command=self.clean_canvas)
        self.clean_button.grid(row=0, column=5)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=6)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.fullscreen = False
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_BLACK
        self.eraser_on = False
        self.active_button = self.pen_button_black
        self.root.bind("<F11>", self.toogle_fullscreen)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.line_width = self.PEN_SIZE


    def use_pen_black(self):
        self.color = self.DEFAULT_BLACK
        self.line_width = self.PEN_SIZE
        self.activate_button(self.pen_button_black)

    def use_pen_red(self):
        self.color = self.DEFAULT_RED
        self.line_width = self.PEN_SIZE
        self.activate_button(self.pen_button_red)

    def use_pen_blue(self):
        self.color = self.DEFAULT_BLUE
        self.line_width = self.PEN_SIZE
        self.activate_button(self.pen_button_blue)

    def use_pen_green(self):
        self.color = self.DEFAULT_GREEN
        self.line_width = self.PEN_SIZE
        self.activate_button(self.pen_button_green)

    def toogle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.c.config(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        else:
            self.c.config(width=600, height=600)

        self.root.attributes("-fullscreen", self.fullscreen)

    def use_eraser(self):
        self.line_width = self.ERASER_SIZE
        self.activate_button(self.eraser_button, eraser_mode=True)

    def clean_canvas(self):
        self.c.delete("all")

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()