from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name =  "index"),#forma de nombrar una ruta
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('user/<int:id>', views.user),
    path('createTask/', views.create_task),
    path('createProject/', views.create_project)

]

