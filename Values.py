values = [1, 3, 4, 7, 0, -9, -8, -3, 10]
Positive_values = []
Negative_values = []
Zero_values = []

for value in values:

    if values > 0:
        Positive_values.append(values)

    elif values < 0:
        Negative_values.append(values)

    else:
        Zero_values.append(values)

print("Positive values:", positive_values)
print("Negative values:", negative_values)
print("Zero values:", zero_values)

print("Counts:", len(positive_values), len(negative_values), len(zero_values)) 