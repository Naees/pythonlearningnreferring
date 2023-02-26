from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/home/Naees/Desktop",
                                          title="Naees File Sorting Program",
                                          filetypes=(("Searching for Python Files", "*.py"),
                                          ("Searching for PNG", "*.png"),
                                          ("Searching for all file types", "*.*"))
                                          ) # this is a linux file path change path accordingly
    # print(filepath)
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()

openBtn = Button(text="Open file explorer", command=openFile)
openBtn.pack() 

window.mainloop()