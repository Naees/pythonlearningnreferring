# text widget = functions like a text area, you can enter multiple lines of text 

from tkinter import *

def submit():
    input = text.get('1.0', END)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Chilanka", 25),
            height=10,
            width=20,
            padx=20,
            pady=20,
            fg="dark blue",)
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()