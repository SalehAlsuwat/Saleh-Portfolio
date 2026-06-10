from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
# Create your views here.

app_name = 'main'

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')


def about_view(request: HttpRequest):
    return render(request, 'main/about.html')


def experience_view(request: HttpRequest):
    return render(request, 'main/experience.html')


def projects_view(request: HttpRequest):
    return render(request, 'main/projects.html')


def skills_view(request: HttpRequest):
    return render(request, 'main/skills.html') 

def contact_view(request: HttpRequest):
    return render(request, 'main/contact.html')


def mode_view(request, mode):

    next_url = request.GET.get("next", "/")

    if mode == "toggle":
        current_mode = request.COOKIES.get("mode", "light")
        mode = "dark" if current_mode == "light" else "light"

    response = redirect(next_url)
    response.set_cookie("mode", mode)

    return response 