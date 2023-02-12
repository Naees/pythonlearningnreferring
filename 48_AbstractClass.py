# Prvents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod     #ABC stands for abstract base classes

class Houses(ABC):
    @abstractmethod
    def type(self):
        pass

class Apartments(Houses):
    def type(self):
        print("These are apartments")

class Shophouses(Houses):
    def type(self):
        print("These are shophouses")

hse = Houses.type()
apt = Apartments.type()
Shphses = Shophouses.type()