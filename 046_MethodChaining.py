# method chaining = calling multiple method sequentially
#                   each acall performs ana ction on the same object and returns self.

class MotorVehicles:
    def turnOn(self):
        print("The vehicle starts up...")
        return self

    def moves(self):
        print("The vehicles moves off..")
        return self
    
    def brake(self):
        print("The vehicle slows down to a stop..")
        return self
    
    def turnOff(self):
        print("The vehicle shuts down..")
        return self


hondacivic = MotorVehicles()

# line by line
hondacivic.moves()
hondacivic.brake()
print()

# method chaining
hondacivic.turnOn().moves().brake().turnOff()
print()
