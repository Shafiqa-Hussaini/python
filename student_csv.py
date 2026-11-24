import pandas as pd
import numpy as np
import math
csv_file = pd.read_csv(r"C:\Users\AUW\Documents\Marks.csv")
print(csv_file)
student = { 
    "name" : "Amina",
    "age" : 20,
    "score" : 78
}


student.update({"score" : 85,
                "major" : "AMDS"})
removed_age = student.pop("age")
print("updated students: ", student)
print("Removed age: ", removed_age )