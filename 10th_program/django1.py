from django.conf import settings
settings.configure(
    DEBUG=True, SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"], MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

posts = []

def home(request):
    html = """
    <h1>Blog Management</h1>

    <form method="post" action="/add/">
    Title: <input name="title"><br><br>
    Content: <textarea name="content"></textarea><br><br>
    <button>Create Post</button>
    </form><hr>
    """

    for i, p in enumerate(posts):
        html += f"""
        <h3>{p['title']}</h3>
        <p>{p['content']}</p>
        <a href="/edit/{i}/">Edit</a> |
        <a href="/delete/{i}/">Delete</a>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        posts.append({
            "title": request.POST["title"],
            "content": request.POST["content"]
        })
    return home(request)

def edit(request, id):
    if request.method == "POST":
        posts[id]["title"] = request.POST["title"]
        posts[id]["content"] = request.POST["content"]
        return home(request)

    return HttpResponse(f"""
    <form method="post">
    Title: <input name="title" value="{posts[id]['title']}"><br><br>
    Content: <textarea name="content">{posts[id]['content']}</textarea><br><br>
    <button>Update</button>
    </form>
    """)

def delete(request, id):
    posts.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line
execute_from_command_line(["program.py", "runserver", "0.0.0.0:8005"])