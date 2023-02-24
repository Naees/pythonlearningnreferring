# Writing files

sampletext = "This file is for the implementation of \n 33_WritingFiles.py"

with open ('test.txt', 'w') as test:    # writing text into a file
    test.write(sampletext)

with open ('test.txt', 'a') as test:    # appending text into a file aka adding more text below
    test.write(sampletext)
