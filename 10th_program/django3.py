from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="search123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path


articles = []


def home(request):

    search = request.GET.get("q", "").lower()

    html = """
    <h1>Article Manager</h1>

    <form method="get">

        <input type="text"
               name="q"
               placeholder="Search article">

        <button>Search</button>

    </form>

    <br>

    <form method="post" action="/new/">

        <input name="title"
               placeholder="Article title">

        <br><br>

        <textarea name="body"
                  placeholder="Article body"></textarea>

        <br><br>

        <button>Add Article</button>

    </form>

    <hr>
    """

    for number, article in enumerate(articles):

        if search and search not in article["title"].lower():
            continue

        html += f"""
        <section>

            <h2>{article["title"]}</h2>

            <p>{article["body"]}</p>

            <a href="/edit/{number}/">
                Modify
            </a>

            |

            <a href="/delete/{number}/">
                Remove
            </a>

        </section>

        <hr>
        """

    return HttpResponse(html)


def new_article(request):

    if request.method == "POST":

        title = request.POST.get("title")
        body = request.POST.get("body")

        articles.append({
            "title": title,
            "body": body
        })

    return home(request)


def edit_article(request, number):

    article = articles[number]

    if request.method == "POST":

        article["title"] = request.POST.get("title")
        article["body"] = request.POST.get("body")

        return home(request)

    return HttpResponse(f"""
        <h1>Modify Article</h1>

        <form method="post">

            <input name="title"
                   value="{article["title"]}">

            <br><br>

            <textarea name="body">{article["body"]}</textarea>

            <br><br>

            <button>Save Article</button>

        </form>

        <br>

        <a href="/">Back</a>
    """)


def delete_article(request, number):

    articles.pop(number)

    return home(request)


urlpatterns = [
    path("", home),
    path("new/", new_article),
    path("edit/<int:number>/", edit_article),
    path("delete/<int:number>/", delete_article),
]


from django.core.management import execute_from_command_line

execute_from_command_line([
    "article.py",
    "runserver",
    "0.0.0.0:8005"
])
