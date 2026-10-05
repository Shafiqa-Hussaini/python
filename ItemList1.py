items = ["book", "chair", "pen", "notebook", "bag", "ERASER"]

item = input("Enter an item: ")

if item.lower() in items:

    print("The item is already available in the list.")

else:

    items.append(item.lower())

    print("The item was not available, so it has been added.")

print("Updated list:", items)