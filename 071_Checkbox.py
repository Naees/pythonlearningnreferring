from tkinter import *

def Display():
    if (x.get()):
        print("You have agreed to the terms and conditions.")
    else:
        print("You have not agreed to the terms and conditions, please accept to continue.")
        
window = Tk()
x = BooleanVar()
# Here are some of the other choices depending on what var you are accepting
# IntVar
# StringVar
image = PhotoImage(file='small_icon.png')
check_button = Checkbutton(window, 
                           text="Click here to accept the terms and conditions.\nMore info below..",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=Display,
                           font=('Comic San', 20),
                           fg='blue',
                           bg="black",
                           activebackground='white',
                           activeforeground='purple',
                           padx=25,
                           pady=10,
                           image=image,
                           compound=LEFT)

check_button.pack()
window.mainloop()