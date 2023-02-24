# 28. String format
# str.format() =    optional method that gives users
#                   more control when displaying output
text = "Ole' MacDonald had a farm!!"


print()
name = "MacDonald"
location = "farm"

#Positional and Keyword arguements
print("Ole' {} had a {}!!".format(name,location))
print("Ole' {1} had a {0}!!".format(location,name))                                 # positional argument
print("Ole' {name} had a {location}!!".format(location="farm",name="MacDonald"))    # keyword argument
print("Ole' {name} had a {name}!!".format(location="farm",name="MacDonald"))        # keyword can be repeated/reused
print()

# Formatting with a string
missingtext = "{} had a little {}!!"
mt1 = "Marry"
mt2 = "lamb"
print(missingtext.format(mt1, mt2))
print()

#Formatting with padding for text
name = "Naees"
print("Hello, my name is {}".format(name))
print("Hello, my name is {name:10}. Nice to meet you!".format(name="Naees"))   #padding
print("Hello, my name is {:<10}. Nice to meet you!".format(name))      #padding with left align
print("Hello, my name is {:>10}. Nice to meet you!".format(name))      #padding with right align
print("Hello, my name is {:^10}. Nice to meet you!".format(name))      #padding with center align
print()


#Formatting for numbers
number = 1000000
print("The number is {:.3f}".format(number))     #displaying in decimal
print("The number is {:,}".format(number))       #displaying , for each thousand
print("The number is {:b}".format(number))       #displaying number in binary
print("The number is {:o}".format(number))       #displaying number in octal
print("The number is {:X}".format(number))       #displaying number in hexadecimal
print("The number is {:E}".format(number))       #displaying number in scientific notation
