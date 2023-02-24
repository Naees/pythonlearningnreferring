# list comprehension =  a way to create a list with less syntax
#                       can mimic certain lambda function, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression (if/else conditional) for item in iterable]

# Part 1: a way to create a list with less syntax
# Code WITHOUT list comprehension
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i*i)     # define what each loop iteration should do
print(squares)

# Code WITH list comprehensions
sq = [i * i for i in range(1,11)]
# expression :  i * i
# for item :    for i in 
# iterable :    range(1,11)
print(squares)


# Part 2: can mimic certain lambda function, easier to read (Lambda vs List comprehension)
# code with lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x : x >= 5, numbers))) # a lambda function making sure the list has only numbers 5 & above

# code with list comprehension 
bmi = [21.87, 26.15, 23.53, 27.04, 31.56, 29.39, 24.14, 22.32, 20.53, 28.26]
healthypeople = [i for i in bmi if i <= 25.0]
print(healthypeople)
flagunhealthy = [i if i >= 25.0 else "HEALTHY" for i in bmi]
print(flagunhealthy)
