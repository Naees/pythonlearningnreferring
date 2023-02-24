# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

rows = int(input("What are the amount of rows required: ")) # what is the count of each column
columns = int(input("What are the amount of columns required: ")) # what is the count of each row
symbol = input("Enter an icon to display: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # use the line "print(symbol)" instead to understand how prints each row and columns 
    print()
