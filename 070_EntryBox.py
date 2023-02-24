from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print(f"Your username is {username}")
    
def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=('Comic Sans', 50),
              fg="#0A0A0A",
              bg="#2D865C",
              show="*")

submitBtn= Button(window, 
                      text=('Submit'),
                      font=('bold'), 
                      command=submit)
delBtn= Button(window, 
                      text='Delete', 
                      command=delete)

bkspBtn= Button(window, 
                      text='Backspace', 
                      command=backspace)
entry.pack()
submitBtn.pack(side=RIGHT)
delBtn.pack(side=RIGHT)
bkspBtn.pack(side=RIGHT)

window.mainloop()