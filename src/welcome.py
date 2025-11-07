from tkinter import *
from tkinter import ttk


def hy(*args):
    print("Hello, World!")

def welcome(root, mainframe):
    ttk.Label(mainframe, text="Hello there").grid(column=3, row=1, sticky=N)

    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Button", command=hy).grid(
        column=3, row=3, sticky=(S, E)
    )

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.columnconfigure(2, weight=1)
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    root.bind("<Return>", hy)
