# canvas = used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

cv = Canvas(window, width=500, height=500)
cv.create_line(0,0,500,500,fill="blue",width=5)
cv.create_line(0,500,500,0, fill="red", width=5)
cv.create_rectangle(50,50,250,250, fill="orange")

point = [250,0,500,500,0,500]
cv.create_polygon(point,fill="brown", outline="black", width=5)

cv.create_arc(0,0,500,500,fill="pink") #style= PIESLICE
cv.create_arc(0,0,500,500,fill="purple", style=CHORD)
cv.create_arc(0,0,500,500,fill="purple", style=ARC)
cv.create_arc(0,0,500,500,fill="red", style=PIESLICE, start=90)
cv.pack()





def show_pokeball():
    # Create a new window to show Pokeball
    pokeball = Toplevel()
    pb = Canvas(pokeball, width=500, height=500)
    pb.create_arc(0, 0, 500, 500, style=PIESLICE, start=360, width=10, extent=180 , fill="red")
    pb.create_arc(0, 0, 500, 500, style=PIESLICE, start=180, width=10, extent=180 , fill="white")
    pb.create_oval(190,190,310,310, fill="white", width=10)
    pb.create_oval(220,220,280,280, fill="light grey", width=10)
    pb.pack()

    # Display the window and start the main event loop
    pokeball.mainloop()

button = Button(window, text="Show Pokeball", command=show_pokeball)
button.pack()

window.mainloop()
