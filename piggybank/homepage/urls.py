from django.urls import path
from . import views

# define list of url patterns

urlpatterns = [
    path('', views.index),
    path('login', views.login),
]