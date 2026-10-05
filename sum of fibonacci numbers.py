n = int(input("Enter n: "))

a = 0
b = 1
sum = 0

for i in range(n):
    sum = sum + a
    a, b = b, a + b

print("Sum of fibonacci numbers: ", sum)