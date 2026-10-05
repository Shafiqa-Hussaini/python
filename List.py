marks = [50, -100, -90, 200, 70, 99, 89, 80]

x = int(input("Enter your mark: "))

if x not in marks:
    print("Mark is not in the list")

else:
    print("Mark is in the list")

    if 0 <= x <= 100:
        print("Valid mark")

        if 97 <= x <= 100:
            print("Grade: A+")
        elif 93 <= x <= 96:
            print("Grade: A")
        elif 90 <= x <= 92:
            print("Grade: A-")
        elif 87 <= x <= 89:
            print("Grade: B+")
        elif 83 <= x <= 86:
            print("Grade: B")
        elif 80 <= x <= 82:
            print("Grade: B-")
        else:
            print("Grade: F")

    else:
        print("Invalid mark")