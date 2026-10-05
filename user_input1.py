while True:
    x = input("Enter your marks: ")

    if not x.isdigit():
        print("Invalid input! Please enter an integer.")
        continue

    x = int(x)

    if x < 0 or x > 100:
        print("Marks must be between 0 and 100.")
        continue

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

    break