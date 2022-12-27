# 35. Move file

import os
src = "test.txt"    # insert full file path if the file is located outside of the project folder
dst = "copy.txt"    # insert full file path if the file is located outside of the project folder

try: 
    if os.path.exists(dst):
        print("File with the same details already exist in the folder!")
    else:
        os.replace(src,dst) # this works for dir similar to how it works for files
        print(f"{src} has been moved!")
except FileNotFoundError:
    print(f"{src} was not found!")