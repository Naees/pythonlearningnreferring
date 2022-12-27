# 31. File detection

import os

filepath = "C:\\Users\\bubbl\\pythonlearningnreferring\\README.md"
folderpath = "C:\\Users\\bubbl\\pythonlearningnreferring"

def linkchecker(path):
    if os.path.exists(path):
        print("This file exist in the system!")
        if os.path.isfile(path):
            print("This is a file!")
        elif os.path.isdir(path):
            print("This is a folder!")
    else:
        print("The thing you are looking for does not exist")

print("File: ")
linkchecker(filepath)
print()
print("Folder: ")
linkchecker(folderpath)