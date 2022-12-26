#   keyword arguements =    arguements preceded by an identifier when we pass them to a function
#                           The order of the arguements doesnt matter, unlike positional arguments
#                           Python knows the names of the arguements that our function receives

def shopInfo(location, level,name):
    print(f"The location of {name} is at {location} on the {level} floor.")

shopInfo(location="Paya Lebar", name="Naes Trading Pte Ltd",level=4)