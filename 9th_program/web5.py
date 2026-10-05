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

students = [
    {"name": "Arun", "age": 20, "course": "Python"},
    {"name": "Priya", "age": 21, "course": "Django"},
    {"name": "Kumar", "age": 19, "course": "Java"},
]


def home(request):
    html = """
    <h1>Student Search</h1>

    <form method="get" action="/">
        <input type="text" name="search" placeholder="Enter student name">
        <button type="submit">Search</button>
    </form>

    <h2>Student List</h2>
    """

    search = request.GET.get("search", "").lower()

    for student in students:
        if search in student["name"].lower():
            html += f"""
            <p>
                <b>{student["name"]}</b> -
                Age: {student["age"]} -
                Course: {student["course"]}
            </p>
            """

    return HttpResponse(html)


urlpatterns = [
    path("", home),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program10.py",
        "runserver",
        "0.0.0.0:8000"
    ])