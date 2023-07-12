from django.shortcuts import render

from django.http import HttpResponse
from .models import project,Task
from django.shortcuts import get_object_or_404,render, redirect
from .forms import CreateNewTask, createNewProject

# Create your views here.
def index(request):
    title = "django course"
    return render(request,"index.html",{
        "title": title
        })

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)

def about(request):
    username = "Jainer"
    return render(request,"about.html", {
        "username" : username
    })


def projects(request):
    projects = project.objects.all()
    return render(request,"projects.html", {
        "projects" : projects
    })

def user (request, id):
    return HttpResponse("<h1>usuario %s<h1>" % id)

def tasks(request):
    tasks = Task.objects.all()
    #task= get_object_or_404(Task, id = id)
    return render(request, "tasks.html",{
        "tasks": tasks
    })

def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html",{
        "form": CreateNewTask()
    })

    else:
         Task.objects.create(title=request.POST["title"], description = request.POST["description"],project_id=2)
         return redirect("/tasks/")


def create_project(request):
    if request.method == "GET":
        return render(request, "create_project.html",{
            "form": createNewProject()
        })
    
    else: 
        projects = project.objects.create(name=request.POST["name"])
        print(projects)
        return render(request, "create_project.html",{
            "form": createNewProject()
        })


