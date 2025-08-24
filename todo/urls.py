
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('todos/create/', views.add_todo, name='create-todo'),
    path('todos/update/<slug:slug>', views.update_todo, name='update_todo'),
    path('todos/delete/<slug:slug>', views.delete_todo, name='delete_todo'),
]
