# TopLevel() =  new window 'on top' of other windows, linked to a 'bottom' window
# Tk() =    new independent window


from tkinter import *

def destroyWindow():
    newer_window.destroy() #destroy closes the window it refers to  

def createTopLvlWindow():
    new_window = Toplevel()

def createTkWindow():
    global newer_window
    newer_window = None
    newer_window = Tk()
    Button(newer_window, text="Close the window using destroy", command=destroyWindow).pack()
    
oldWindow = Tk()

Button(oldWindow, text="Click here to create a new TopLevel window..", command=createTopLvlWindow).pack()
Button(oldWindow, text="Click here to create a new Tk window..", command=createTkWindow).pack()

oldWindow.mainloop()


