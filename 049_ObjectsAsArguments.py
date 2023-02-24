class RoadBikes:
    gears = "Low"

class FixedGearBikes:
    gears = "Low"

def changeGears(bikes, gears):
    bikes.gears = gears
    print(f"The gears of the bike have been changed to {gears}")


cipollini = RoadBikes()
cinelli = FixedGearBikes()
print("Before using objects as arguements:")
print(cipollini.gears)
print(cinelli.gears)

print("\nAfter using objects as arguements as an example: ")

changeGears(cinelli, "Middle")
changeGears(cipollini, "High")

print("\n",cinelli.gears)
print(cipollini.gears)
