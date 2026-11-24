items = {
    "book": 100,
    "pen": 20,
    "chair": 500,
    "bag": 800
}

item = input("Enter an item: ")

if item in items:
    print(f"The price of {item} is {items[item]}")
else:
    price = float(input("Item is not available. Enter the price: "))
    items[item] = price
    print(f"The price of {item} is {items[item]}")