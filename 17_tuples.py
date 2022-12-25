# tuple =   collection which is ordered and unchangeable used to group together related data

citizeninfo = ("Naes", 22, "male")


# Here are some methods for tuples
print("Display the amount of times Naes appears in the tuple: " + str(citizeninfo.count("Naes")))
print("Display the index/position where 22 appears in the tuple: " + str(citizeninfo.index(22)))

print()

print("Display citizen information")
for x in citizeninfo:
    print(x)

print()

if "Naes" in citizeninfo:
    print("Records of Naes has been found in the tuple")