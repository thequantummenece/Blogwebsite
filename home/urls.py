from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('' ,views.home,name = "home"),
    path('about', views.about,name = "about"),
    path('contact', views.contact,name = "contact"),
    path('search',views.search,name = "search"),
    path('signin',views.signin,name = "signin"),
    path('blogin',views.blogin,name = "blogin"),
    path('blogout',views.blogout,name = "blogout")
]
