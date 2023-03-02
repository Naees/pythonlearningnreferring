from tkinter import *
from time import *

def update():
    timeNow = strftime("%I:%M:%S %p")
    timeLbl.config(text=timeNow)
    
    dayNow = strftime("%A")
    dayLbl.config(text=dayNow)
    
    dateNow = strftime("%d %B %Y")
    dateLbl.config(text=dateNow)
    
    window.after(1000,update)

window = Tk()

timeLbl = Label(window, font=("Comic Sans",50), fg="red", bg="black")
timeLbl.pack()

dayLbl = Label(window, font=("Ink Free",25 ), fg="black")
dayLbl.pack()

dateLbl = Label(window, font=("Ink Free",19 ), fg="black")
dateLbl.pack()

update()

window.mainloop()