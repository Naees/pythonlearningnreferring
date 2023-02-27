from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure in a parent

window = Tk()

titleLbl = Label(window, text="Enter personal information here: ", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

fNameLbl = Label(window, text="First name: ", width=20, bg="blue").grid(row=1, column=0)
fNameEntry = Entry(window).grid(row=1, column=1)

lNameLbl = Label(window, text="Last name: ", bg="red").grid(row=2, column=0)
lNameEntry = Entry(window).grid(row=2, column=1)

mailLbl = Label(window, text="Email: ",width=30, bg="green").grid(row=3, column=0)
mailEntry = Entry(window).grid(row=3, column=1)

submitBtn = Button(window, text="Submit Now", width=30).grid(row=4, column=0, columnspan=2)

window.mainloop()