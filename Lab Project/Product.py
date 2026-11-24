Prices = {"pen": 15, "book": 120, "bag": 850}

Requested_items = {"book", "ruler", "pen"}

for item in Requested_items:
    price = Prices.get(item)
    if price is not None:
        print(f"{item}: Tk {price}")
    else:
        print(f"{item}: not found")


    