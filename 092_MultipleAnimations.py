from tkinter import *
import time
from Ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

basket = Ball(canvas, 0, 0, 100, 1, 2, "brown")
pingpong = Ball(canvas, 0, 0, 30, 4, 3, "white")
base = Ball(canvas, 0, 0, 40, 4, 4, "red")

while True:
    basket.move()
    pingpong.move()
    base.move()
    window.update()
    time.sleep(0.01)

window.mainloop()