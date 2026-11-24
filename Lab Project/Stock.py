stock = {"pen": 12, "book": 3, "bag": 2, "ruler": 9, "calculator": 1}

total_units = sum(stock.values())
low_stock = {}

for product, quantity in stock.items():
    if quantity < 5:
        low_stock[product] = quantity

print("Total units:", total_units)
print("Low stock:", low_stock)