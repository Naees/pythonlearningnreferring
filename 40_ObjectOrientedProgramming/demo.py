from roomba import Roomba


# def __init__(self, weight, batteries, quantity, rating, brand):
hseholdroomba = Roomba(4.65, "Yes", 5443, "Positive", "XiaoMi")
factoryprototype = Roomba(5.32,"Yes", 234, "Negative", "Zoomeras")

print(hseholdroomba.weight)
print(hseholdroomba.batteriesRequired)
print(hseholdroomba.quantity)
print(hseholdroomba.rating)
print(hseholdroomba.brand)
print("\n\n")
print(factoryprototype.weight)
print(factoryprototype.batteriesRequired)
print(factoryprototype.quantity)
print(factoryprototype.rating)
print(factoryprototype.brand)
print("\n\n")
hseholdroomba.startCleaning()
factoryprototype.stopCleaning()