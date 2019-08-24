from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox

class Paint(object):

    PEN_SIZE = 2.0
    ERASER_SIZE = 20.0
    DEFAULT_BLACK = 'black'
    DEFAULT_RED = 'red'
    DEFAULT_BLUE = 'blue'
    DEFAULT_GREEN = 'green'

    def __init__(self):
        self.root = Tk()
        self.action_frame = Frame(self.root)
        self.action_frame.grid(row=0, column=0, sticky='wen')

        self.pen_button_black = Button(self.action_frame, 
            text='B', 
            bg=self.DEFAULT_BLACK, fg=self.DEFAULT_BLACK, 
            cursor="hand2", 
            command=self.use_pen_black
        )
        self.pen_button_black.grid(row=0, column=0)

        self.pen_button_red = Button(self.action_frame, 
            text='R', 
            bg=self.DEFAULT_RED, 
            fg=self.DEFAULT_RED, 
            cursor="hand2",
            command=self.use_pen_red
        )
        self.pen_button_red.grid(row=0, column=1)

        self.trashIcon = PhotoImage(file="./icons/trash.png")
        self.eraseIcon = PhotoImage(file="./icons/eraser.png")
        self.browserIcon = PhotoImage(file="./icons/browser.png")

        self.pen_button_blue = Button(self.action_frame, text='B', cursor="hand2", bg=self.DEFAULT_BLUE, fg=self.DEFAULT_BLUE, command=self.use_pen_blue)
        self.pen_button_blue.grid(row=0, column=2)

        self.pen_button_green = Button(self.action_frame, text='G', cursor="hand2", bg=self.DEFAULT_GREEN, fg=self.DEFAULT_GREEN, command=self.use_pen_green)
        self.pen_button_green.grid(row=0, column=3)

        self.eraser_button = Button(self.action_frame, compound=CENTER, image=self.eraseIcon, width="25",height="25", text='', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=4)

        self.clean_button = Button(self.action_frame, compound=CENTER, image=self.trashIcon, width="25",height="25", text='', command=self.clean_canvas)
        self.clean_button.grid(row=0, column=5)

        self.browser_button = Button(self.action_frame, compound=CENTER, image=self.browserIcon, width="25",height="25", text='', command=self.drawn_browser)
        self.browser_button.grid(row=0, column=6)

        self.draw_frame = Frame(self.root)
        self.draw_frame.grid(row=1, column=0, sticky='nwse')

        self.c = Canvas(self.draw_frame, bg='white', cursor='cross')
        self.c.grid(row=0, sticky='nwse')

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.fullscreen = False
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_BLACK
        self.eraser_on = False
        self.active_button = self.pen_button_black
        self.root.bind("<F12>", self.quit)
        self.root.bind("<F11>", self.toogle_fullscreen)
        self.root.bind("<Escape>", self.toogle_fullscreen)
        self.root.bind("<F5>", self.clean_canvas)
        self.root.bind("<F1>", self.help)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.line_width = self.PEN_SIZE


    def use_pen_black(self):
        self.color = self.DEFAULT_BLACK
        self.line_width = self.PEN_SIZE
        self.activate_button(self.pen_button_black)

    def help(self, event=None):
        messagebox.showinfo("Help","""
        <f12> Fecha o programa\n
        <f11> Tela Cheia\n
        <Esc> Tela Cheia\n
         <f5> Limpa Tela\n
         <f1> Ajuda\n
        """)

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
            self.c.config(width=self.root.winfo_width(), height=self.root.winfo_height())

        self.root.attributes("-fullscreen", self.fullscreen)

    def quit(self, event=None):
       self.root.destroy()

    def use_eraser(self):
        self.line_width = self.ERASER_SIZE
        self.activate_button(self.eraser_button, eraser_mode=True)

    def drawn_browser(self):
        self.c.delete("all")
        self.c.create_line(0, 20, self.root.winfo_width(), 20)
        self.c.create_line(0, 60, self.root.winfo_width(), 60)
        self.c.create_line(10, 0, 10, 20)
        self.c.create_line(10, 60, self.root.winfo_width(), 60)

    def clean_canvas(self, event=None):
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