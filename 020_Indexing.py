# 20. Indexing
# index operator [] = gives access to a sequence's element (str, list, tuples)

vidgame = 'tabs Totally Accurate Battle Simulator!'

if(vidgame[0].islower()):
    vidgame = vidgame.capitalize()
print(vidgame)
print()

first = vidgame[:3].upper()
last = vidgame[4:].lower()
lChar = vidgame[-1]

print(first)
print(last)
print(lChar)
