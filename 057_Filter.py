# filter() = creates a collection of elements from a iterable fro which a function returns

# filter(function, iterable)


# a filter function to ensure that the people on the guest list are legal for entry ino the club
guestlist = [("Alice", 18), ("Bob", 19), ("Charlie", 20), ("David", 21), ("Eve", 22)]
legal_age_checker = print(tuple(filter(lambda x: x[1] >= 18, guestlist)))


# a filter function to check if the int are even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
