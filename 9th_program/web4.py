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


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        tamil = int(request.POST.get("tamil"))
        english = int(request.POST.get("english"))
        maths = int(request.POST.get("maths"))

        total = tamil + english + maths
        average = total / 3

        if average >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        return HttpResponse(f"""
            <h1>Student Result</h1>

            <p><b>Name:</b> {name}</p>
            <p>Tamil: {tamil}</p>
            <p>English: {english}</p>
            <p>Maths: {maths}</p>

            <hr>

            <p><b>Total:</b> {total}</p>
            <p><b>Average:</b> {average:.2f}</p>
            <p><b>Result:</b> {result}</p>

            <br>
            <a href="/">Back</a>
        """)

    return HttpResponse("""
        <h1>Student Result Management</h1>

        <form method="post">

            Name:
            <input type="text" name="name"><br><br>

            Tamil:
            <input type="number" name="tamil"><br><br>

            English:
            <input type="number" name="english"><br><br>

            Maths:
            <input type="number" name="maths"><br><br>

            <button type="submit">
                Calculate Result
            </button>

        </form>
    """)


urlpatterns = [
    path("", home),
]


from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program12.py",
        "runserver",
        "0.0.0.0:8000"
    ])