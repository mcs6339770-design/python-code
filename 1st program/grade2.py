marks = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    marks.append(int(input("Enter mark: ")))

total = sum(marks)
average = total / n

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade) 