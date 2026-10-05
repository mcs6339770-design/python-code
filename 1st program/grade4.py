def find_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    marks.append(int(input("Enter mark: ")))

total = sum(marks)
average = total / n
grade = find_grade(average)

print("Total:", total)
print("Average:", average)
print("Grade:", grade)