# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Sword:
    def slashing(self):
        print("You are slashing the SWORD..")
    
    def defend(self):
        print("You are blocking with the SWORD..")
        
class Axe:
    def slashing(self):
        print("You are slashing the AXE..")
    
    def defend(self):
        print("You are blocking with the AXE..")

class Claymore:
    def slashing(self):
        print("You are slashing the CLAYMORE..")
    
    def defend(self):
        print("You are blocking with the CLAYMORE..")

class Player():
    def executeMove(self, weapon):
        weapon.slashing()
        weapon.defend()
        print("You have finished your current turn.. PLEASE WAIT FOR THE NEXT TURN..")
        

sword = Sword()
axe = Axe()
longsword = Claymore()
timmy = Player()
timmy.executeMove(longsword)
print()
timmy.executeMove(axe)
print()
timmy.executeMove(sword)
