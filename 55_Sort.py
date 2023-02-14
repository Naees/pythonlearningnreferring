# sort() method = used with list
# sort() function = used with iterables

# PART 1
# Sorted method
listbikes = ["Aleoca", "Polygon", "Pinarello", "Trek", "Factor"]
tuplebikes = ("Aleoca", "Polygon", "Pinarello", "Trek", "Factor") # This demo of tuple will not work as error cause tuple objects does not have a sort function.
listbikes.sort()
# tuplebikes.sort() It does not work with tuples ERROR ERROR ERROR
for i in listbikes:
    print(i)
print()

# Sorted method with Reverse arguement
listbikes.sort(reverse=True)
for i in listbikes:
    print(i)
print()

# Sorted function
sortedlistbike = sorted(tuplebikes) # This sorted function works with tuples
for i in sortedlistbike:
    print(i)
print()

# PART 2
healthstatus = [("Joshua", "E1", 20), ("Sebas", "B4", 21), ("Julian", "B2", 21), ("Zane", "E9",20), ("WF", "B1", 21)]
healthstatus.sort()
for i in healthstatus:
    print(i)
print()

# with key
sortedby = lambda status: status[1]
healthstatus.sort(key=sortedby)
for i in healthstatus:
    print(i)
print()

# with key and reverse
sortedby = lambda status: status[2]
healthstatus.sort(key=sortedby)
for i in healthstatus:
    print(i)
print()

# Sorting a nested tuple using sorted function
tuplehealthstatus = (("Joshua", "E1", 20), ("Sebas", "B4", 21), ("Julian", "B2", 21), ("Zane", "E9",20), ("WF", "B1", 21))
sortedby = lambda status: status[2]
sortedhealthstatustuple = sorted(tuplehealthstatus, key=sortedby)
for i in sortedhealthstatustuple:
    print(i)