class Bike:

    def __init__(self,make, model, speed, price, rating):
        self.make = make        # instance variable (affects that specific instance)
        self.model = model      # instance variable
        self.speed = speed      # instance variable
        self.price = price      # instance variable
        self.rating = rating    # instance variable

    wheels = 2                  # class variable (affects the whole class)