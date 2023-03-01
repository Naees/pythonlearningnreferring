from tkinter import *

def clicker(event):
    print(f"Mouse coordinates: \n X Cord: {str(event.x)}\n Y Cord: {str(event.y)} ")
    
def clickerRelease(event):
    print(f"Mouse btn released")
    
def clickerEnter(event):
    print(f"Cursor re-entered window")
    
def clickerLeave(event):
    print(f"Cursor left window")

window = Tk()

window.bind("<Button-1>",clicker) # left mouse click
window.bind("<Button-2>",clicker) # scroll wheel mouse click
window.bind("<Button-3>",clicker) # right mouse click
window.bind("<ButtonRelease>",clickerRelease) #  release of a button
window.bind("<Enter>",clickerEnter) #  Entering cursor on window
window.bind("<Leave>",clickerLeave) #  Leaving cursor on window
# window.bind("<Motion>",clicker) #  Leaving cursor on window

window.mainloop()