import matplotlib.pyplot as plt

# Runtime input
n = int(input("Enter number of students: "))

students = []
hours = []

for i in range(n):
    name = input("Enter student name: ")
    hour = float(input("Enter study hours: "))
    students.append(name)
    hours.append(hour)

# Create dashboard
plt.figure(figsize=(12, 4))

# 1. Line Chart
plt.subplot(1, 3, 1)
plt.plot(students, hours, marker="o")
plt.title("Study Hours Trend")
plt.xlabel("Students")
plt.ylabel("Hours")
plt.xticks(rotation=45)

# 2. Bar Chart
plt.subplot(1, 3, 2)
plt.bar(students, hours)
plt.title("Study Hours Comparison")
plt.xlabel("Students")
plt.ylabel("Hours")
plt.xticks(rotation=45)

# 3. Pie Chart
plt.subplot(1, 3, 3)
plt.pie(hours, labels=students, autopct="%1.1f%%")
plt.title("Study Hours Distribution")

plt.tight_layout()
plt.show()