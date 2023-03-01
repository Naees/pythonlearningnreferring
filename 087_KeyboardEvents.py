from tkinter import *

def keyPress(event):
    #print(f"You pressed: {event.keysym}")
    lbl.config(text=event.keysym)

window = Tk()

window.bind("<Key>",keyPress)

lbl = Label(window,font=("Comic Sans",100))
lbl.pack()

window.mainloop()

