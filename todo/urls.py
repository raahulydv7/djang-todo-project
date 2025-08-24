
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('create/', views.add_todo, name='create-todo'),
    path('update/<slug:slug>', views.update_todo, name='update_todo'),
]
