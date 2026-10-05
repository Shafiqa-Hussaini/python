numbers=[-1,2,3,4,-2,-5,-10]
positives=[]
negatives=[]
for number in numbers:
    if number>0:
        positives.append(number)
    else:
        negatives.append(number)

print("positive numbers:", positives)
print("negative numbers:", negatives)