from tkinter import *

def openFile():
    print("File has been opened")
    
def saveFile():
    print("File has been saved")
    
def cutFile():
    print("File has been cut")
    
def copyFile():
    print("File has been copy")
    
def pasteFile():
    print("File has been paste")
    


window = Tk()

saveicon = PhotoImage(file="save.png")
# saveicon = saveicon.zoom(50)
saveicon = saveicon.subsample(15,15)
fileicon = PhotoImage(file="file.png")
fileicon = fileicon.subsample(15,15)

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))

menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image= fileicon, compound=LEFT)
fileMenu.add_command(label="Save", command=saveFile, image=saveicon, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cutFile)
editMenu.add_command(label="Copy", command=copyFile)
editMenu.add_command(label="Paste", command=pasteFile)


window.mainloop()