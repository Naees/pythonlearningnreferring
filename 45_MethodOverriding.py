class Cyclist:
    def rides(self):
        print("The bike is moving..")

class Communter(Cyclist):
    def rides(self):
        print("The bike travels with extra loads..")

john = Communter()
john.rides()