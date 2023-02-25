# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():
    # print(f"You have submitted {listbox.get(listbox.curselection())}")    # for single selection without multiple
    
    
    transportation = list(listbox.curselection())
    print("Here are your selections on modes of travel: ")
    count = 1
    for index in transportation:
        print(f"{count}. Selection No. {index}: {listbox.get(index)}")
        count += 1
    
def add():
    print(f"You have added {listbox.get(listbox.curselection())}")
    listbox.insert(listbox.size(), entryBx.get())
    listbox.config(height=listbox.size())
    
def delete():
    # print(f"You have deleted {listbox.get(listbox.curselection())}")
    # listbox.delete(listbox.curselection())
    count = 1
    print("Here is the list of deleted commutes: ")
    for index in reversed(listbox.curselection()):
        print(f"{count}. Selection No. {index}: {listbox.get(index)}")
        listbox.delete(index)
        count += 1
        # add deleted list
    listbox.config(height=listbox.size())
    
window = Tk()

listbox = Listbox(window,
                  bg="#FFF1DC",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Car")
listbox.insert(2, "Bus")
listbox.insert(3, "Train")
listbox.insert(4, "Bicycle")
listbox.insert(5, "Motorcycle")
listbox.insert(6, "Boat")
listbox.insert(7, "Airplane")

listbox.config(height=listbox.size())

entryBx = Entry(window)
entryBx.pack()

submitBtn = Button(window, text="Submit commute", command=submit)
submitBtn.pack()

addBtn = Button(window, text="Add new commute", command=add)
addBtn.pack()

delBtn = Button(window, text="Delete the commute", command=delete)
delBtn.pack()


window.mainloop()