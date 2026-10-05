while True:
    try:
        x = int(input("Enter your marks:"))
    except ValueError:
        print("It is not an integer.")
        print("please enter an integer.")
        continue
    if x < 0 or x > 100:
        print("The marks must be between 0 and 100.")
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


