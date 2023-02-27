from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt", 
                                    filetypes=[("Save as text file", ".txt"),
                                              ("Save as HTML file", ".html"),
                                              ("Save as any file", ".*")])
    filetext = str(text.get(1.0, END))
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