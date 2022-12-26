# 27. kwargs
#   **kwargs =  parameter that will pack all arguements into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments

def shopInfo(**kwargs): # you don't have to specifically name the parameter as kwargs but ensure that one must have "**"
    print(f"The location of {kwargs['Shop_name']} is at {kwargs['Location']} on the {kwargs['Level']} floor.")
    print()
    print("Detailed shop information: ")
    for x,y in kwargs.items():
        print(x,y)

shopInfo(Location="Paya Lebar", Shop_name="Naes Trading Pte Ltd",Level=4, Pax="Crowded", Disabilities="Accessable")