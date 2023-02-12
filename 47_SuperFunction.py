# super () =    Function used to give access to the method of a parent class.
#               Returns a temporary object of a parent class when used

class Shapes:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Shapes):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def area(self):
        return self.length  *   self.width

class Cuboid(Shapes):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.height * self.height

sq = Square(5,5)
cube = Cuboid(5,5,5)

print(sq.area())
print(cube.volume())