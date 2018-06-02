# prevent-gui-from-resize
import tkinter as tk
win = tk.Tk()
win.title("Python GUI")
win.resizable(0,0) #set window coordinates to (0,0)
win.mainloop()
