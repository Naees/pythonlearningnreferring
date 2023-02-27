from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of window/display

oneTab = Frame(notebook) # new frame for tab 1
twoTab = Frame(notebook) # new frame for tab 2

notebook.add(oneTab, text="Tab One")
notebook.add(twoTab, text= "Tab Two")
notebook.pack(expand=True, fill='both') # expand to fill any space not otherwise used
                                        # fill = fill space on x and y axis

Label(oneTab, text="This is the first tab", width=50, height=25).pack()
Label(twoTab, text="This is the second tab", width=50, height=25).pack()


window.mainloop()