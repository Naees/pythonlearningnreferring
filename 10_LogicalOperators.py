# 10. logical operators

# logical operats (and,or,not) = used to check if two or more conditional statements

temp = int(input("What is the temperature outside?: "))

if (temp>=0 and temp<= 30):
  print("The temperature is good today!")
  print("Go outside")
  print()

elif (temp < 0 or temp >30):
  print("The temperature is bad today!")
  print("Stay inside")
  print()


# not operator example
if not(temp>=0 and temp<= 30):
  print("The weather is bad today!")
  print("Lets stay at home")