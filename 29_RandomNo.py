# 29. Random number

import random

# Returns a random number between the given range
x = random.randint(1,6)
# Returns a random float number between 0 and 1
y = random.random()
print(x,y)
print()

# Returns a random element from the given sequence
randcolor = ['Black', 'Blue', 'Green', 'Purple']
z = random.choice(randcolor)
print(z)
print()

# Takes a sequence and returns the sequence in a random order
hexa = [1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
random.shuffle(hexa)
print(hexa)