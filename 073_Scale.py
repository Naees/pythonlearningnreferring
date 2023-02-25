from tkinter import *

def submit():
    print(f"You have travelled {str(scale.get())}KM today.")

window = Tk()

rdmicon = PhotoImage(file='small_icon.png')
rdmLbl = Label(image = rdmicon)
rdmLbl.pack()

scale = Scale(window,
              from_=100,
              to_=0,
              length=600,
              orient=VERTICAL, #Orientation of the scale
              font = ('Comic sans', 15),
              tickinterval= 10, # add numeric indicator for value
              # showvalue=0, # hide the current value that follows along the slider
              resolution= 5 , #increment of slider
              troughcolor = '#EDF1D6',
              fg = '#40513B',
              bg = '#9DC08B',
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # set current value of slider
scale.pack()

bikeImg = PhotoImage(file='bikeicon.png')
bikeLbl = Label(image = bikeImg)
bikeLbl.pack()


btn = Button(window, 
             text='Submit Distance', 
             command=submit)
btn.pack()

window.mainloop()