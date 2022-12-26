# *args =   parameter that will pack all arguements into a tuple
#           useful so that a function can accept a varying amout of arguements

def sumofnumbers(*args): #*args can be different parameter
    sum = 0
    addition = list(args)   # as you can't alter the information in the tuple "*args variable", there is a need to cast "*args" into a list for editing
    addition[0] = 20
    for i in addition:
        sum += i
    return sum

print(sumofnumbers(1,1,1,1))