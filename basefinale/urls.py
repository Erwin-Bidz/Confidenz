from django.urls import path

from basefinale import admin, views

urlpatterns = [
    path('', views.home, name= "home")
]
