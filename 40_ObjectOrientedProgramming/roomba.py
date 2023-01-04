class Roomba:

    def __init__(self, weight, batteries, quantity, rating, brand):
        self.weight = weight
        self.batteriesRequired = batteries
        self.quantity = quantity
        self.rating = rating
        self.brand = brand

    def startCleaning(self):
        print(f"The {self.brand} roomba has left the startion and is starting to clean the area.")

    def stopCleaning(self):
        print(f"The {self.brand} roomba has finished cleaning and is returning back to the station.")