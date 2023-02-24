# map() =   applies a function to each item in an iterable (list, tuples, etc.)
# map(function, iterable)

fruits = [("apple", 1.50), ("banana", 0.50), ("orange", 2.00), ("kiwi", 1.00), ("grape", 1.75)]

def add_tax(item):
    name, price = item
    name = name.capitalize()
    tax = price * 0.08
    total_price = round(price + tax,2)
    print(f"The price of the {name} is ${total_price}.")
    return (name, total_price)


items_with_tax = list(map(add_tax, fruits))

# for items in items_with_tax:
#     print(items)
