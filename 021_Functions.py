# function = a block of code which is executed only when it is called.
# When functions are def, you will need to call the function to use it.

def my_first_function():
    print("This is my first function!")
    print("Yay!")
    print()
my_first_function()

# functions with user input
def a_function_with_inputs(username):
    print(f"Hi my name is {username}")
    print()

userinput= input("What is your name: ")
a_function_with_inputs(userinput)

#functions with multiple preset variables
def func_with_multiple_variables(fname, lname, age):
    print(f"Hello {fname} {lname}, you are {age} years old!")
    print("Thank you for your time :) ")
func_with_multiple_variables("Whip", "Nae Nae", 22)

