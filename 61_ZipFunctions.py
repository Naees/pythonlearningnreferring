# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ['jdoe', 'asmith', 'mrodriguez', 'rbrown', 'tnguyen']
passwords = ['p@ssw0rd', 's3cret', 'changeme', 'letmein', 'secure123']
userData = zip(usernames, passwords, range(1, len(usernames)+1))
print("Welcome to the Usernames & Passwords database")
for i in userData:
    print(f"{i[2]}. {i[0]}: {i[1]}")

# userData is a ZIP data type:
print(f"\n As you can see here userData is a ZIP data type: \n{type(userData)}\n")

# to convert it to a list, tuple or other data type you can use this command below
userData = list(userData)
print(type(userData))
userData = list(zip(usernames, passwords, range(1, len(usernames)+1)))
print(type(userData))

# here is how to convert it into a dict
userData = dict(zip(usernames, passwords))
for key,value in userData.items():
    print(key, value)

print(type(userData))