# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entierly
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

while True:
    favnumber = input("What is your most favourite whole number: ")
    if favnumber != "":
        break

social_security_num = "111-22-3333"

for i in social_security_num:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,10): # lets say I would like to ignore all even number iteration of the for loop I will use the pass loop control statement
    if (i % 2) == 0:
        pass
    else:
        print(i)
