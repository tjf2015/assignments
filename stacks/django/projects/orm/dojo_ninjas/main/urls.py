from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path("dojo", views.dojo),
    path("ninja", views.ninja),
    path("tryagain", views.tryagain),
    path('delete', views.delete)
]