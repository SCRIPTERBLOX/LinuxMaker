from tkinter import *
from tkinter import ttk

from welcome import welcome


root = Tk()
root.title("LinuxMaker")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

if __name__ == "__main__":
    welcome(root, mainframe)

root.mainloop()
