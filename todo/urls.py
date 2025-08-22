
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home, name='home'),
    path('register/', views.register_user, name='register'),

]
