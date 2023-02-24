# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Grandparent:
    alive = True

class Parent(Grandparent):
    def middleage(self):
        print(f"This parent is in the middle of the family tree!")

class Child(Parent):
    def youngest(self):
        print(f"This child is the youngest in the family!")


timmy = Child()
print(timmy.alive)
timmy.middleage()
timmy.youngest()
