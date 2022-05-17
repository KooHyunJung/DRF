from django.urls import path

from accountapp.views import hello_world_drf, BooksAPI, BookAPI

urlpatterns = [
    path('hello_world_drf/', hello_world_drf),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
]
