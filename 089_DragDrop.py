from tkinter import *

def dragStart(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    
def dragMotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

lbl = Label(window, bg="red", width=10, height=5)
lbl.place(x=0,y=0)

lbl2 = Label(window, bg="blue", width=10, height=5)
lbl2.place(x=100,y=100)

lbl.bind("<Button-1>",dragStart)
lbl.bind("<B1-Motion>",dragMotion)

lbl2.bind("<Button-1>",dragStart)
lbl2.bind("<B1-Motion>",dragMotion)

window.mainloop()