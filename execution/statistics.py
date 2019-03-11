from tkinter import *
from tkinter import ttk


def hello():
    print("hello!")


def stats_window(sim, win):

    nb = ttk.Notebook(win)
    nb.pack()

    # Make 1st tab
    f1 = Frame(nb)
    # Add the tab
    nb.add(f1, text="First tab")

    # Make 2nd tab
    f2 = Frame(nb)
    # Add 2nd tab
    nb.add(f2, text="Second tab")

    nb.select(f2)

    nb.enable_traversal()