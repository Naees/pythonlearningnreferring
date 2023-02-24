# list = used to store multiple items in a single variable
print()
flowers = ["Roses", "Lily", "Tulips", "To Be Removed"]
print("Before list controls:")
for i in range(len(flowers)):
    print(flowers[i])
print()

# add values to a list
flowers.append("Hyacinth") 
print("Appending:")
for i in range(len(flowers)):
    print(flowers[i])
print()

# remove values from a list
flowers.remove("To Be Removed") 
print("Removed:")
for i in range(len(flowers)):
    print(flowers[i])
print()

# remove the last element from the list
flowers.pop()
print("Pop:")
for i in range(len(flowers)):
    print(flowers[i])
print()

# insert a value into a specific place in the list
flowers.insert(1, "Peruvian Lily")
print("Insert:")
for i in range(len(flowers)):
    print(flowers[i])
print()

# sort the list
flowers.sort()
# Parameters for sort:
# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison
print("Sort:")
for i in range(len(flowers)):
    print(flowers[i])
print()

# clear the list
flowers.clear()
print("Clear:")
for i in range(len(flowers)):
    print(flowers[i])
print()
