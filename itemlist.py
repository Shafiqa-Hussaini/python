items = ["book", "chair", "pen", "notebook", "bag"]

item = input("Enter an item: ")

if item in items:
    print("The item is already available in the list.")
else:
    items.append(item)
    print("The item was not available, so it has been added")

print("updated list: ", items)