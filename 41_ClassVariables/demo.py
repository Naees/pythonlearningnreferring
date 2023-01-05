from bike import Bike

# def __init__(self,make, model, speed, price, rating):

colnago = Bike("Colnago", "V4Rs", 18, 9847.01, "Positive")
pinarello = Bike("Pinarello", "F12", 21, 19847.01, "Mostly-Positive")
babybike = Bike("Aleoca", "XCVVX-192", 1, 270, "Negative")

babybike.wheels = 4 #lets just say that a baby bike has training wheels which add the total amt of wheels to 4

# both would show the default 2 wheels
print(colnago.wheels)
print(pinarello.wheels)

# this would show the altered 4 wheels
print(babybike.wheels)

Bike.breaks = "Dura Ace BR-R9200"
print(Bike.breaks)