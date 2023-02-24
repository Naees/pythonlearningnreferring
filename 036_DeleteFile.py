# 35. Delete file
import os
import shutil

# for files
# file does not remove empty folder
try:
    location = "copy.txt"
    os.remove(location)
except FileNotFoundError:
    print("This file does not exist!")
except PermissionError:
    print(f"User does not have permission to delete {location}")
else:
    print(f"{location} has been deleted!")

# for directory
# directory will not be delete if it contain files
try:
    path = "some_empty_folder"
    os.rmdir(path) # directory will not be delete if it contain files
    shutil.rmtree(path) # the alternative to os.rmdir, it will dir with files in it. (CONSIDERED DANGEROUS)
except FileNotFoundError:
    print("This dir does not exist!")
except PermissionError:
    print(f"User does not have permission to delete {path}")
except OSError:
    print(f"User is unable to delete the dir while using this function")
else:
    print(f"{path} has been deleted!")
