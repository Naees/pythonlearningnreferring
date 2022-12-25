#   dictionary =    A changeable, unordered collection of unique key: value pairs
#                   Fast because they use hashing, allow us to access a value quickly

singapore = {'North-east':'Sengkang',
                'North':'Woodlands',
                'South':'Keppel'}

#print(singapore['South']) this will encounter an error if the key of the dictionary does not exist
print("Get method: ")
print(singapore.get('West'))
print(singapore.get('North-east'))
print()

print("Method for getting all the keys")
print(singapore.keys())
print()

print("Method for getting all the values")
print(singapore.values())
print()

print("Method for printing the whole dictionary")
print(singapore.items())
print()

print("For loop with dictionaries")
for x,y in singapore.items():
    print(x, y)
print()

print("A method to updates values using a key in the dictionary")
singapore.update({'South': 'Deport Road'})
singapore.update({'West': 'Bukit Timah'})
print(singapore.items())
print()

print("Method for popping")
singapore.pop('West')
print(singapore.items())
print()

print("Method for clearing the dictionary")
singapore.clear()
print(singapore.items())
print()


