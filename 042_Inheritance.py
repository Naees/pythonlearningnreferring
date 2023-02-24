class Motorvehicles:    # parent

    started = True

    def accelerate(self):
        print("The motor vehicle proceeds to accelerate!")

    def decelerate(self):
        print("The motor vehicle slows down!")



class Car(Motorvehicles):   #child
    def characteristics(self): 
        print("It moves quick")

class Truck(Motorvehicles):   #child
    def characteristics(self): 
        print("Good storage")

class Bus(Motorvehicles):   #child
    def characteristics(self): 
        print("Transporting a good amount of passengers")

class Van(Motorvehicles):   #child
    def characteristics(self): 
        print("Good general transporting vehicle")

hondacivic = Car()
toyotahiace = Van()
mercedescitaro = Bus()

print(hondacivic.started)
hondacivic.accelerate()
toyotahiace.decelerate()
mercedescitaro.characteristics()
