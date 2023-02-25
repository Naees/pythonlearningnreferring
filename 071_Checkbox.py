from tkinter import *

def Display():
    if (x.get()==1):
        print("You have agreed to the terms and conditions.")
    else:
        print("You have not agreed to the terms and conditions, please accept to continue.")

window = Tk()
x = IntVar()
check_button = Checkbutton(window, 
                           text="Click here to accept the terms and conditions.\nMore info below..",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command= Display)

check_button.pack()
window.mainloop()