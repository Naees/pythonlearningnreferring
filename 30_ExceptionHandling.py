# Exception Handling

#exception = events detected during execution that interrupts the flow of a program
while True:
    try:
        numerator = int(input("Enter a number: "))
        denominator = int(input("Divided by: "))
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Number can't be divided by 0!!")
    except ValueError:
        print("The entry is not a number!!")
    except Exception:
        print("ERROR SPOTTED AHHHHH")
    else:
        print(result)   # Does not execute if an exception has been caught
    finally:
        print("This will always execute whether or not we have encountered an exception")