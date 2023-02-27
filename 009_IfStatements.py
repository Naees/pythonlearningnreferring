# 9. if statements

# if statements = a block of ccode that will execute if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
  print("You are a century old!: ")
elif age >= 18:
  print("You are an adult!")
elif age < 0:
  print("You haven't been born yet!")
else:
  print("You are a child!")
