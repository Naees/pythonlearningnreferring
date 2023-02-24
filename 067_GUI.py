from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Naes's first GUI program")

icon = PhotoImage(file="tokyoskytree.png")
window.iconphoto(True,icon)
window.config(background="black") # it can be a color or the hex color code of a color like "#5cfcff"

window.mainloop() #place window on computer screen, listen for events
