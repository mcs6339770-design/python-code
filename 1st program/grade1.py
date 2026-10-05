n = int(input("Enter number of subjects: "))
total = 0
i = 1

while i <= n:
    mark = int(input("Enter mark: "))
    total += mark
    i += 1

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

print("Total:", total)
print("Average:", average)
print("Grade:", grade)