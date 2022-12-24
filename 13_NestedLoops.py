# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

rows = int(input("What are the amount of rows required: "))
columns = int(input("What are the amount of columns required: "))
symbol = input("Enter an icon to display: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()