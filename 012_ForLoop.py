# 12. for loop

import time

# for loop = a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
#for loop = limited

for index in range(10):
  print(index+1)

for index in range (500,100,-2):
  print(index)

for index in "Sean Er":
  print(index)

for seconds in range(10,0,-1):
  print(seconds)
  time.sleep(1)
print("Happy New Year!")
