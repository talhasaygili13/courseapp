from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("anasayfa", views.home),
    path("kurslar", views.kurslar),
]

