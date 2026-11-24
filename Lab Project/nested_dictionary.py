scores = {
    "Amina": {"python": 82, "statistics": 76, "calculus": 88},
    "Maya": {"python": 58, "statistics": 64, "calculus": 61},
    "Disha": {"python": 91, "statistics": 89, "calculus": 94},
    "Nora": {"python": 45, "statistics": 52, "calculus": 56}
}

results = {}
top_student = None
highest_avg = -1

for student, subjects in scores.items():
    avg = round(sum(subjects.values()) / len(subjects), 2)
    status = "Pass" if avg >= 60 else "Fail"
    
    results[student] = {
        "average": avg,
        "status": status
    }
    
    if avg > highest_avg:
        highest_avg = avg
        top_student = student

print("Results:", results)
print("Top student:", top_student)