# adding a label to gui

import tkinter as tk
from tkinter import ttk #ttk = themed tk

win = tk.Tk() # win is short for windows #constructor
win.title("Python GUI with label")
ttk.Label(win, text="A Label").grid(column=0, row=0) #set label text name an grid coordinates
win.mainloop()
