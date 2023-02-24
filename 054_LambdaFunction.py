# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# 
# 
# lambda parameter:expression

double = lambda x : print(x * 2)
multiply = lambda x , y: print(x * y)
add = lambda x, y, z:print(x + y + z)
fullname = lambda firstname, lastname: print(f"{firstname} {lastname}")
illegalage = lambda age: print(True if age >= 18 else False)
bmichecker = lambda bmi: print("Overweight" if bmi > 25.0 else "Healthy or Underweight")

double(2)
multiply(2,5)
add(1,2,3)
illegalage(17)
illegalage(20)
bmichecker(17)
bmichecker(26)
