# Higher Order Function =   a function that either:
#                           1.  accepts a function as an arguement
#                               #
#                           2.  returns a function
#                               (In python, functions are also treated as objects)


# (DEMO) 1.  accepts a function as an arguement
def highSoundLevels(output):
    return output.upper()

def lowSoundLevels(output):
    return output.lower()

def sampleFunction(func):
    text = func("This is some sample output..")
    print(text)

sampleFunction(highSoundLevels)



# (DEMO) 2.  returns a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))
