values = [1, 3, 4, 7, 0, -9, -8, -3, 10]

positive_values = []
negative_values = []
zero_values = []

for value in values:
    if value > 0:
        positive_values.append(value)
    elif value < 0:
        negative_values.append(value)
    else:
        zero_values.append(value)

print("Positive values:", positive_values)
print("Negative values:", negative_values)
print("Zero values:", zero_values)

print("Counts:", len(positive_values), len(negative_values), len(zero_values))