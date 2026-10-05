from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="blog123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path


posts = {}
count = 0


def home(request):

    html = """
    <h1>Simple Blog</h1>

    <form action="/add/" method="post">

        <input name="title"
               placeholder="Enter title">

        <br><br>

        <textarea name="content"
                  placeholder="Enter content"></textarea>

        <br><br>

        <button>Add Post</button>

    </form>

    <hr>
    """

    for key, post in posts.items():

        html += f"""
        <div>

            <h2>{post["title"]}</h2>

            <p>{post["content"]}</p>

            <a href="/edit/{key}/">
                Edit
            </a>

            |

            <a href="/delete/{key}/">
                Delete
            </a>

        </div>

        <hr>
        """

    return HttpResponse(html)


def add_post(request):

    global count

    if request.method == "POST":

        count += 1

        posts[count] = {
            "title": request.POST.get("title"),
            "content": request.POST.get("content")
        }

    return home(request)


def edit_post(request, key):

    if key not in posts:
        return HttpResponse("Post does not exist")

    if request.method == "POST":

        posts[key]["title"] = request.POST.get("title")
        posts[key]["content"] = request.POST.get("content")

        return home(request)

    post = posts[key]

    return HttpResponse(f"""
        <h1>Edit Post</h1>

        <form method="post">

            Title:
            <input name="title"
                   value="{post["title"]}">

            <br><br>

            Content:
            <textarea name="content">{post["content"]}</textarea>

            <br><br>

            <button>Update Post</button>

        </form>

        <br>

        <a href="/">Home</a>
    """)


def delete_post(request, key):

    if key in posts:
        del posts[key]

    return home(request)


urlpatterns = [
    path("", home),
    path("add/", add_post),
    path("edit/<int:key>/", edit_post),
    path("delete/<int:key>/", delete_post),
]


from django.core.management import execute_from_command_line

execute_from_command_line([
    "blog.py",
    "runserver",
    "0.0.0.0:8005"
])
