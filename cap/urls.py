from django.urls import path

from . import  views

urlpatterns = [

    path("cap/", views.cap),

    path("home/",views.home),
    path("about/",views.about),
]
