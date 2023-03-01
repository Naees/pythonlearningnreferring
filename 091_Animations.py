from tkinter import *
import time

# Set window dimensions and initial velocity of the astronaut
WIDTH = 478
HEIGHT = 478
xVelocity = 3
yVelocity = 1

# Create the main window
window = Tk()

# Create a canvas that fills the entire window
spaceCanvas = Canvas(window, width=WIDTH, height=HEIGHT)
spaceCanvas.pack()

# Load the space background image and resize it to fill the canvas
space = PhotoImage(file="planets.png")
space = space.zoom(2,2)
spacebg = spaceCanvas.create_image(0,0,image=space, anchor=NW)

# Load the astronaut image and resize it
astronaut = PhotoImage(file="astronaut.png")
astronaut = astronaut.subsample(8,8)
player = spaceCanvas.create_image(0,0,image=astronaut, anchor=NW)

# Get the dimensions of the astronaut image
playerWidth = astronaut.width()
playerHeight = astronaut.height()

# Animation loop
while True:
    # Get the current coordinates of the astronaut
    coordinates = spaceCanvas.coords(player)
    
    # If the astronaut hits the left or right edge of the canvas, reverse the x velocity
    if (coordinates[0] >= WIDTH - playerWidth or coordinates[0] < 0):
        xVelocity = xVelocity * -1
    
    # If the astronaut hits the top or bottom edge of the canvas, reverse the y velocity
    if (coordinates[1] >= HEIGHT - playerHeight or coordinates[1] < 0):
        yVelocity = yVelocity * -1
    
    # Move the astronaut by its current velocity
    spaceCanvas.move(player, xVelocity, yVelocity)
    
    # Update the window and wait a short amount of time before updating again
    window.update()
    time.sleep(0.01)

# Start the tkinter main loop
window.mainloop()

# from tkinter import *
# import time


# WIDTH = 500
# HEIGHT = 500
# xVelocity = 3
# yVelocity = 1

# window = Tk()

# spaceCanvas = Canvas(window, width=WIDTH, height=HEIGHT)
# spaceCanvas.pack()


# space = PhotoImage(file="planets.png")
# spacebg = spaceCanvas.create_image(0,0,image=space, anchor=NW)

# astronaut = PhotoImage(file="astronaut.png")
# astronaut = astronaut.subsample(8,8)
# player = spaceCanvas.create_image(0,0,image=astronaut, anchor=NW)


# playerWidth = astronaut.width()
# playerHeight = astronaut.height()
# while True:
#     coordinates = spaceCanvas.coords(player)
#     print(coordinates)
#     if (coordinates[0]>=WIDTH-playerWidth or coordinates[0]<0):
#         xVelocity = xVelocity * -1
#     if (coordinates[1]>=HEIGHT-playerHeight or coordinates[1]<0):
#         yVelocity = yVelocity * -1
#     spaceCanvas.move(player,xVelocity, yVelocity)
#     window.update()
#     time.sleep(0.01)
    
# window.mainloop()