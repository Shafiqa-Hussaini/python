people = list(range(1, 1001))

round_number = 1

while len(people) > 1:
    people = people[1::2]

    print("Round", round_number)
    print(people)
    print("Number of people:", len(people))

    round_number += 1

print("Last person:", people[0])