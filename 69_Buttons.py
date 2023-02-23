from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(f"Here are some information about the form, You have selected the button {count} number of times.")
    
window = Tk()

photo = PhotoImage(file='tokyoskytree.png')

button = Button(window, 
                text='Click here for more information..', 
                command=click,
                fg="black",
                bg="white",
                font=('Comic Sans', 40),
                activebackground='black',
                activeforeground='white',
                image=photo,
                compound='right')

button.pack()
window.mainloop()