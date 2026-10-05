import matplotlib.pyplot as plt

# Runtime input
n = int(input("Enter number of students: "))

students = []
marks = []

for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    students.append(name)
    marks.append(mark)

# Create dashboard
plt.figure(figsize=(12, 4))

# 1. Line Chart
plt.subplot(1, 3, 1)
plt.plot(students, marks, marker="o")
plt.title("Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)

# 2. Bar Chart
plt.subplot(1, 3, 2)
plt.bar(students, marks)
plt.title("Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)

# 3. Pie Chart
plt.subplot(1, 3, 3)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Marks Distribution")

plt.tight_layout()
plt.show()