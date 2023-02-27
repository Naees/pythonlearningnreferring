from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/home/naees/Desktop",
                                    defaultextension=".txt", 
                                    filetypes=[("Save as text file", ".txt"),
                                              ("Save as HTML file", ".html"),
                                              ("Save as any file", ".*")])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = input("Enter the text that you want to be saved: ")
    file.write(filetext)
    file.close()

window = Tk()

btnSave = Button(window, 
                 text="Save file here..", 
                 command=saveFile)
btnSave.pack()
text = Text(window)
text.pack()

window.mainloop()