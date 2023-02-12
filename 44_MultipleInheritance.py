# multiple inheritance = when a chiled class is derived from more than one parent class

class Prey:
    def flee(self):
        print("Fleeing..")

class Predator:
    def hunt(self):
        print("Hunting..")

class Rat(Prey):
    pass

class Eagle(Predator):
    pass

class Fishes(Prey, Predator):
    pass

rat = Rat()
eagle = Eagle()
fish = Fishes()

rat.flee()
eagle.hunt()
fish.flee()
fish.hunt()