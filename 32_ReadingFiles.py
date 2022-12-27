# Reading files
try:
    with open('README.md') as rm: # with open helps to close the file after operation
        print(rm.read())
except FileNotFoundError:
    print("This file does not exist, ohhh no!!")
# print(file.closed) # only need when the file is not opened as demostrated above