# reduce() =    apply a function to an iterable and reduce it to a single cumilative value.
#               performs function on first two elements and repeats process until 1 value remains

import functools

# a reduce function that helps to multiple all int in the list
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product)

# a reduce function that join all the letters of the word together
letter = ["H", "E", "L", "L", "O"]
combined = functools.reduce(lambda x, y: x + y ,letter)
print(combined)
