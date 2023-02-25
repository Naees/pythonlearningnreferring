# radio imagebutton = similar to checkbox, but you can only select one from a group
from tkinter import *

transportation = ['Car', 'Bus', 'Train', 'Bicycle']

# def order():
#     if (X.get()):
#         print(f"You have ordered {X.get(transportation[index])}")

def order():
    if X.get() != -1: # check if a radio button has been selected
        print(f"You have ordered {transportation[X.get()]}")
    else:
        print("Please select a transportation option.")


window = Tk()
X = IntVar()

bus = PhotoImage(file='bikeicon.png')
train = PhotoImage(file='bikeicon.png')
car = PhotoImage(file='bikeicon.png')
bike = PhotoImage(file='bikeicon.png')
icons = [car, bus, train, bike]
for index in range(len(transportation)):
    transportationOptions = Radiobutton(window, 
                                    text=transportation[index], 
                                    variable=X, 
                                    value=index,
                                    font=('Impact', 50),
                                    image=icons[index], # adding images using the for loop
                                    compound='left',
                                    indicatoron=0, # eliminate circle indicators
                                    width=375, # width of radio btns
                                    command=order
                                    )

    transportationOptions.pack(anchor=W)
    
window.mainloop()

    