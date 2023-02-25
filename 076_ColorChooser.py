from tkinter import *
from tkinter import colorchooser # submodule

def enable():
    color = colorchooser.askcolor() # assign color to a variable
    print(color)
    colorHex = color[1] # assigns element at index 1 to a variable
    print(colorHex)
    window.config(bg=color[1]) # change background color

window = Tk()
window.geometry("500x500")
startBtn = Button(text="Enable Color Picker", command=enable)
startBtn.pack()
window.mainloop()