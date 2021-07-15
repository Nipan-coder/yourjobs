from django.urls import path, include
from app import views


urlpatterns = [
    path('',views.Home, name="home"),
    path('post/',views.Post, name="post"),
    path('search/',views.scarch, name='search'),
]