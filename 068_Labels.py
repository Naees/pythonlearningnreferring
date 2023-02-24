from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='tokyoskytree.png')

label = Label(window,
              text="Tokyo Skytree with cute softtoys \n<3", 
              font=('Arial', 40, 'bold'), 
              fg='#00FF00', 
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='left',)
label.pack()
# label.place(x=100, y=100)  # it allows you to place the x and y value of the label

window.mainloop()
