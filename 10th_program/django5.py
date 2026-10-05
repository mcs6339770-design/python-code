from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="abc123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

blogs = []
next_id = 1


def home(request):
    page = """
    <h1>My Blog</h1>

    <form action="/create/" method="post">
        <input type="text" name="title" placeholder="Blog Title"><br><br>

        <textarea name="content"
                  placeholder="Write your blog"></textarea><br><br>

        <button type="submit">Publish</button>
    </form>

    <hr>
    """

    for blog in blogs:
        page += f"""
        <article>
            <h2>{blog["title"]}</h2>
            <p>{blog["content"]}</p>

            <a href="/update/{blog["id"]}/">Edit</a>
            |
            <a href="/remove/{blog["id"]}/">Delete</a>
        </article>

        <hr>
        """

    return HttpResponse(page)


def create(request):
    global next_id

    if request.method == "POST":
        blogs.append({
            "id": next_id,
            "title": request.POST.get("title"),
            "content": request.POST.get("content")
        })

        next_id += 1

    return home(request)


def update(request, blog_id):

    blog = next(
        (x for x in blogs if x["id"] == blog_id),
        None
    )

    if blog is None:
        return HttpResponse("Blog not found")

    if request.method == "POST":
        blog["title"] = request.POST.get("title")
        blog["content"] = request.POST.get("content")

        return home(request)

    return HttpResponse(f"""
        <h1>Edit Blog</h1>

        <form method="post">

            Title:
            <input name="title"
                   value="{blog["title"]}">

            <br><br>

            Content:
            <textarea name="content">{blog["content"]}</textarea>

            <br><br>

            <button>Save Changes</button>

        </form>
    """)


def remove(request, blog_id):

    global blogs

    blogs = [
        blog for blog in blogs
        if blog["id"] != blog_id
    ]

    return home(request)


urlpatterns = [
    path("", home),
    path("create/", create),
    path("update/<int:blog_id>/", update),
    path("remove/<int:blog_id>/", remove),
]


from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py",
    "runserver",
    "0.0.0.0:8005"
])
