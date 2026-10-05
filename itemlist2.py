items = ["BOOK", "Chair", "Pen", "Notebook", "Bag"]

item = input("Enter an item: ")

if item.lower() in [x.lower() for x in items]:

    print("The item is already available in the list.")

else:

    items.append(item)

    print("The item was not available, so it has been added.")

print("Updated list:", items)