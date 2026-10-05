import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="student123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[],
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
    ],
)

django.setup()

from django.http import HttpResponse
from django.urls import path

students = []


def home(request):
    html = """
    <h1>Student Management</h1>

    <form method="post" action="/add/">
        Name:
        <input type="text" name="name"><br><br>

        Age:
        <input type="number" name="age"><br><br>

        Course:
        <input type="text" name="course"><br><br>

        <button type="submit">Add Student</button>
    </form>

    <h2>Student List</h2>
    """

    for i, student in enumerate(students):
        html += f"""
        <p>
            <b>{student["name"]}</b>
            - Age: {student["age"]}
            - Course: {student["course"]}

            <a href="/edit/{i}/">Edit</a>
            <a href="/delete/{i}/">Delete</a>
        </p>
        """

    return HttpResponse(html)


def add_student(request):
    if request.method == "POST":
        students.append({
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "course": request.POST.get("course")
        })

    return home(request)


def edit_student(request, id):

    student = students[id]

    if request.method == "POST":
        student["name"] = request.POST.get("name")
        student["age"] = request.POST.get("age")
        student["course"] = request.POST.get("course")

        return home(request)

    return HttpResponse(f"""
        <h1>Edit Student</h1>

        <form method="post">

            Name:
            <input type="text"
                   name="name"
                   value="{student['name']}"><br><br>

            Age:
            <input type="number"
                   name="age"
                   value="{student['age']}"><br><br>

            Course:
            <input type="text"
                   name="course"
                   value="{student['course']}"><br><br>

            <button type="submit">Update</button>
        </form>

        <br>
        <a href="/">Back</a>
    """)


def delete_student(request, id):
    students.pop(id)
    return home(request)


urlpatterns = [
    path("", home),
    path("add/", add_student),
    path("edit/<int:id>/", edit_student),
    path("delete/<int:id>/", delete_student),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program11.py",
        "runserver",
        "0.0.0.0:8000"
    ])