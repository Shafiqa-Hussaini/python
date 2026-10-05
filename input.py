x = ""

while not x.isdigit():
    x = input("Enter your marks: ")

    if not x.isdigit():
        print("Invalid input! Please enter an integer.")

x = int(x)

print("Type:", type(x))

if 97 <= x <= 100:
    print("Grade: A+")
elif 93 <= x <= 96:
    print("Grade: A")
elif 90 <= x <= 92:
    print("Grade: A-")
elif 87 <= x <= 89:
    print("Grade: B+")
else:
    print("Grade: F")