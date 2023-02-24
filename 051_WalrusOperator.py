# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

wishlist = list()
# while True:
#    wishes = input("What do you like?: ")
#    if wishes == "quit":
#     break    
#     foods.append(food)

while (wishes := input("What would you like to add to your wishlist: ").capitalize()) != "Quit":
    print(f"{wishes} has been added to the wishlist..\n")
    wishlist.append(wishes)

for i in wishlist:
    print(i)

print(wishlist)
