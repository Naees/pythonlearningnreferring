from tkinter import *
from tkinter.ttk import *

import time

def startProg():
    gb = 100
    download = 0
    speed = 1
    while (download<gb):
        time.sleep(0.05)
        progBar['value']+= (speed/gb)*100
        download+=1
        percent.set(str(int((download/gb)*100))+"%")
        text.set(str(download)+"/"+str(gb)+" GB downloaded")
        window.update_idletasks()
    

window =Tk()

percent = StringVar()
text = StringVar()

progBar = Progressbar(window, orient=HORIZONTAL, length=300)
progBar.pack()

progLbl = Label(window, textvariable=percent).pack()
taskLbl = Label(window, textvariable=text).pack()

btn = Button(window, text="download", command=startProg).pack()

window.mainloop()