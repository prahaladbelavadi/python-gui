# creating butotns and changing their texts
import tkinter as tk
from tkinter import ttk #ttk = themed tk

win = tk.Tk() # win is short for windows #constructor
win.title("Python GUI with label")
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(foreground='red')

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)
win.mainloop()
