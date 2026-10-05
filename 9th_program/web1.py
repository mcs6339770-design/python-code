import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="mysecretkey",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
    ],
)

django.setup()

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path


# Temporary student data
students = [
    {
        "id": 1,
        "name": "Arun",
        "age": 20,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 21,
        "course": "Django"
    }
]


def home(request):

    html = """
    <html>
    <head>
        <title>Student Management</title>
    </head>

    <body>

        <h1>Student Management System</h1>

        <h2>Add New Student</h2>

        <form action="/add/" method="POST">

            <label>Name:</label>
            <input type="text" name="name" required>
            <br><br>

            <label>Age:</label>
            <input type="number" name="age" required>
            <br><br>

            <label>Course:</label>
            <input type="text" name="course" required>
            <br><br>

            <input type="submit" value="Add Student">

        </form>

        <hr>

        <h2>Students</h2>

        <table border="1" cellpadding="10">

            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
                <th>Course</th>
                <th>Action</th>
            </tr>
    """

    for student in students:

        html += f"""
            <tr>

                <td>{student["id"]}</td>

                <td>{student["name"]}</td>

                <td>{student["age"]}</td>

                <td>{student["course"]}</td>

                <td>
                    <a href="/edit/{student["id"]}/">
                        Edit
                    </a>

                    |

                    <a href="/delete/{student["id"]}/">
                        Delete
                    </a>
                </td>

            </tr>
        """

    html += """
        </table>

    </body>
    </html>
    """

    return HttpResponse(html)


def add_student(request):

    if request.method == "POST":

        new_student = {
            "id": len(students) + 1,
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "course": request.POST.get("course")
        }

        students.append(new_student)

    return redirect("/")


def edit_student(request, student_id):

    student = None

    for item in students:
        if item["id"] == student_id:
            student = item
            break

    if student is None:
        return HttpResponse("Student not found")

    if request.method == "POST":

        student["name"] = request.POST.get("name")
        student["age"] = request.POST.get("age")
        student["course"] = request.POST.get("course")

        return redirect("/")

    html = f"""
    <html>

    <body>

        <h1>Edit Student</h1>

        <form method="POST">

            <label>Name:</label>
            <input type="text"
                   name="name"
                   value="{student["name"]}"
                   required>

            <br><br>

            <label>Age:</label>
            <input type="number"
                   name="age"
                   value="{student["age"]}"
                   required>

            <br><br>

            <label>Course:</label>
            <input type="text"
                   name="course"
                   value="{student["course"]}"
                   required>

            <br><br>

            <button type="submit">
                Update Student
            </button>

        </form>

        <br>

        <a href="/">
            Back to Home
        </a>

    </body>

    </html>
    """

    return HttpResponse(html)


def delete_student(request, student_id):

    for student in students:

        if student["id"] == student_id:
            students.remove(student)
            break

    return redirect("/")


urlpatterns = [

    path("", home),

    path("add/", add_student),

    path("edit/<int:student_id>/", edit_student),

    path("delete/<int:student_id>/", delete_student),

]


from django.core.management import execute_from_command_line


if __name__ == "__main__":

    execute_from_command_line([
        "program11.py",
        "runserver",
        "0.0.0.0:8000"
    ])
