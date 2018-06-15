# check boxes

import tkinter as tk
from tkinter import ttk #ttk = themed tk

win = tk.Tk() # win is short for windows #constructor
win.title("Python GUI with label textbox widgets")
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

#button on click function
def clickMe(): #function to change contents of object on click
    action.configure(text="Hello " + name.get() + " " + numberChosen.get())
    aLabel.configure(foreground='red')
    action.grid(column=2, row=0)

# button
action = ttk.Button(win, text="Click Me!", command=clickMe) # on click of button that says click me, call function clickMe
action.grid(column=2, row=1) #location of button

# Number dropdown label
ttk.Label(win,text='Choose a number:').grid(column=1,row=0) #set label text and location
number = tk.StringVar() # typesetting number as a string
numberChosen= ttk.Combobox(win, width=12, textvariable=number, state='readonly`')
numberChosen['values'] = (1, 2, 4, 42, 100) # list of dropdown options
numberChosen.grid(column=1,row=1) #location of dropdown option
numberChosen.current(3) #prechosen number

# Text box label
ttk.Label(win, text="Enter a name:").grid(column=0,row=0) #location of the text label

# Input box
name = tk.StringVar() # set type of input of name as string
nameEntered = ttk.Entry(win, width=12, textvariable=name) # take input from application
nameEntered.grid(column=0,row=1) #location of input box
nameEntered.focus()

#checkboxes
chVarDis = tk.IntVar() # typeset variable to expect integer
#first checkbox
check1 = tk.Checkbutton (win,text="Disabled", variable=chVarDis, state='disabled') # disabled text and state is disabled
check1.select() #select implies the box is checked
check1.grid(column=0, row=4, sticky=tk.W) #location of checkbox

# # second check box
# chVarUn = tk.IntVar()
# check2 = Checkbutton (win, text="Unchecked", variable=chVarUn)
# check2.deselect()
# check2.grid(columnn=1, row=4, sticky=tk.W)
#
# # third checkbox
# chVarEn = tk.IntVar()
# check3 = Checkbutton (win, text="Enabled", variable=chVarEn)
# check3.select()
# check3.grid(columnn=2, row=4, sticky=tk.W)

#radio buttons
# Radiobutton global
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

#Radiobutton Callback
def radCall():
    radSel=radVar.get()
    radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)
# create 3 radiobuttons
radVar = tk.IntVar()


win.mainloop()
