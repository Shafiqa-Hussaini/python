items = ["apple", "banana", "orange"]

item = input("Enter an item: ")

if item in items:
    print("Item is already available in the list.")
else:
    items.append(item)
    print("Item was not available, so it has been added.")

print("Updated list:", items)