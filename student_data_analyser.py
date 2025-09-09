import numpy as np
import pandas as pd


marks = np.random.randint(0,101 , size = (10,5))
student = [f"Student {i+1}" for i in range(10)]
subject = ["Maths","Science","EVS","PPS","Python"]
df = pd.DataFrame(marks , index = student, columns = subject)

print(df)

df["Total"] = df.sum(axis =1)
df["average"] = df.mean(axis = 1)

subject_avg =df[subject].mean()
Topper = df["Total"].idxmax() 
topper_marks = df.loc[Topper]

def getGrade(avg):
    if avg >=90:
        return "A"
    elif avg>= 75:
        return "B"
    elif avg>= 60:
        return "C"
    elif avg>= 45:
        return "D"
    else:
        return "F"
    
df["Grade"] = df["average"].apply(getGrade)

print("\n Student Marks Table:\n")
print(df)

print("\n Subject-wise Average Marks:\n")
print(subject_avg)

print(f"\n Topper: {Topper}")
print("Their Marks:\n", topper_marks)