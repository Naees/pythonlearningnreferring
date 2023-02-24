# Nested Functions Call

# Nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

# num = input("Enter a whole number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

#The same of what is written above can be represented below through the use of nested function calls

print(round(abs(float(input("Enter a whole positive number: ")))))
