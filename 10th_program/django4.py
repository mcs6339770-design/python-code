from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="django456",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path


class BlogStore:

    posts = []

    @classmethod
    def add(cls, title, content):

        cls.posts.append({
            "title": title,
            "content": content
        })

    @classmethod
    def get(cls, index):

        return cls.posts[index]

    @classmethod
    def delete(cls, index):

        cls.posts.pop(index)


def home(request):

    output = """
    <h1>Class Based Blog</h1>

    <form action="/save/" method="post">

        <input name="title"
               placeholder="Title">

        <br><br>

        <textarea name="content"
                  placeholder="Content"></textarea>

        <br><br>

        <button>Save</button>

    </form>

    <hr>
    """

    for index, post in enumerate(BlogStore.posts):

        output += f"""
        <h2>{post["title"]}</h2>

        <p>{post["content"]}</p>

        <a href="/change/{index}/">
            Edit
        </a>

        |

        <a href="/remove/{index}/">
            Delete
        </a>

        <hr>
        """

    return HttpResponse(output)


def save(request):

    if request.method == "POST":

        BlogStore.add(
            request.POST.get("title"),
            request.POST.get("content")
        )

    return home(request)


def change(request, index):

    post = BlogStore.get(index)

    if request.method == "POST":

        post["title"] = request.POST.get("title")
        post["content"] = request.POST.get("content")

        return home(request)

    return HttpResponse(f"""
        <h1>Change Blog</h1>

        <form method="post">

            <input name="title"
                   value="{post["title"]}">

            <br><br>

            <textarea name="content">{post["content"]}</textarea>

            <br><br>

            <button>Update</button>

        </form>
    """)


def remove(request, index):

    BlogStore.delete(index)

    return home(request)


urlpatterns = [
    path("", home),
    path("save/", save),
    path("change/<int:index>/", change),
    path("remove/<int:index>/", remove),
]


from django.core.management import execute_from_command_line

execute_from_command_line([
    "blog.py",
    "runserver",
    "0.0.0.0:8005"
])
