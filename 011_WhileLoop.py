# 11. while loop

# while loop = a statement that will execute it's block of code, as long as it's condition remains true. 

name = ""

while len(name) == 0:
  name = input("What is your name: ")
  if len(name)!=0:
    print ("Your name is "+name)
    break

print("Program Ended!")
