delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}

combined_delivery = delivery_1.copy()

for product, quantity in delivery_2.items():
    combined_delivery[product] = combined_delivery.get(product, 0)

grand_total = sum(combined_delivery.values())

print("Combined delivery: ", combined_delivery)
print("Grand total:", grand_total)