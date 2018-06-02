# combining box widgets

import tkinter as tk
from tkinter import ttk #ttk = themed tk

win = tk.Tk() # win is short for windows #constructor
win.title("Python GUI with label textbox widgets")
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickMe(): #function to change label on click
    action.configure(text="Hello " + name.get() + " " + numberChosen.get())
    aLabel.configure(foreground='red')
    action.grid(column=2, row=0)

action = ttk.Button(win, text="Click Me!", command=clickMe) # on click of button that says click me, call function clickMe
action.grid(column=2, row=1) #location of button

ttk.Label(win,text='Choose a number:').grid(column=1,row=0)
number = tk.StringVar()
numberChosen= ttk.Combobox(win, width=12, textvariable=number, state='readonly`')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1,row=1)
numberChosen.current(3)

ttk.Label(win, text="Enter a name:").grid(column=0,row=0) #location of the text label

name = tk.StringVar() # set type of input of name as string
nameEntered = ttk.Entry(win, width=12, textvariable=name) # take input from application
nameEntered.grid(column=0,row=1) #location of input box
nameEntered.focus()

win.mainloop()
