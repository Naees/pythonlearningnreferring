from tkinter import *

def moveUp(event):
    lbl.place(x=lbl.winfo_x(), y=lbl.winfo_y()-10)
    
def moveDown(event):
    lbl.place(x=lbl.winfo_x(), y=lbl.winfo_y()+10)
    
def moveLeft(event):
    lbl.place(x=lbl.winfo_x()-10, y=lbl.winfo_y())
    
def moveRight(event):
    lbl.place(x=lbl.winfo_x()+10, y=lbl.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",moveUp)
window.bind("<a>",moveLeft)
window.bind("<s>",moveDown)
window.bind("<d>",moveRight)
window.bind("<Up>",moveUp)
window.bind("<Left>",moveLeft)
window.bind("<Down>",moveDown)
window.bind("<Right>",moveRight)

img = PhotoImage(file='bikeicon.png')
lbl = Label(window, image=img)
lbl.place(x=0,y=0)

window.mainloop()