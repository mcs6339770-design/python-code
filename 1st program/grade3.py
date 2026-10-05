subjects = ["Python", "Maths", "English", "Science", "Computer"]
total = 0

for subject in subjects:
    mark = int(input("Enter " + subject + " mark: "))
    total += mark

average = total / len(subjects)

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

print("\nTotal =", total)
print("Average =", average)
print("Grade =", grade)