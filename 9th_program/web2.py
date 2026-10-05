import os
import django
from django.conf import settings

# Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='student123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'students.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

students = []

def home(request):
    html = """
    <h1>Student Record Management</h1>

    <form method="post" action="/add/">
        Name: <input type="text" name="name"><br><br>
        Age: <input type="number" name="age"><br><br>
        Course: <input type="text" name="course"><br><br>
        <button type="submit">Add Student</button>
    </form>

    <h2>Student List</h2>
    """

    for i, student in enumerate(students):
        html += f"""
        <p>
        <b>{student['name']}</b> -
        Age: {student['age']} -
        Course: {student['course']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a>
        </p>
        """

    return HttpResponse(html)


def add_student(request):
    if request.method == "POST":
        student = {
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "course": request.POST.get("course")
        }

        students.append(student)

    return home(request)


def detail(request, id):
    student = students[id]

    return HttpResponse(f"""
    <h1>Student Details</h1>
    <p>Name: {student['name']}</p>
    <p>Age: {student['age']}</p>
    <p>Course: {student['course']}</p>
    <a href="/">Back</a>
    """)


def delete_student(request, id):
    students.pop(id)
    return home(request)


urlpatterns = [
    path('', home),
    path('add/', add_student),
    path('detail/<int:id>/', detail),
    path('delete/<int:id>/', delete_student),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program9.py",
        "runserver",
        "0.0.0.0:8000"
    ])