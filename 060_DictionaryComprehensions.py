# dictionary comprehension =    create dictionaries using an expression
#                               can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

# lets create a dictionary comprehension that adds additional tax on the prices (8% GST)
# dictionary = {key: expression for (key, value) in iterable}
fruitsPrices = {"apples": 10, "bananas": 5, "cherries": 20, "dates": 7, "elderberries": 3}
fruitsPricesWithTax = {key: round((value * 1.08),2) for (key, value) in fruitsPrices.items()}
print(fruitsPricesWithTax)

# lets create a dictionary comprehension WITH ADDITIONAL IF CONDITIONAL that checks for weather
# dictionary = {key: expression for (key, value) in iterable if conditional}
weather = {
    "New York": "Sunny",
    "Los Angeles": "Cloudy",
    "Chicago": "Rainy",
    "Miami": "Thunderstorm",
    "Seattle": "Rainy"
}
badWeatherChecker = {key:value for (key, value) in weather.items() if value == "Rainy"}
print(badWeatherChecker)

# lets create a dictionary comprehension WITH ADDITIONAL IF & ELSE CONDITIONAL to flag if the location is Cold, Warm or Hot
# dictionary = {key: (if/else) for (key, value) in iterable}

temps = {
    "New York": 8,
    "Los Angeles": 21,
    "Chicago": 4,
    "Houston": 17,
    "Phoenix": 24,
    "Philadelphia": 6,
    "San Antonio": 15
}
tempsChecker = {key: ("WARM!!" if value > 15 else "COLD!!") for (key, value) in temps.items()}
print(temps)
print(tempsChecker)

# lets create a dictionary comprehension with a function 
# dictionary = {key: function(value) for (key, value) in iterable}

def check_temp(value):
    if value > 25:
        return "Hot weather"
    elif 20 >= value <=25:
        return "Warm weather"
    else:
        return "Cold weather"

desc_cities = lambda x: print({key: check_temp(value) for (key, value) in temps.items()})
desc_cities(temps)
