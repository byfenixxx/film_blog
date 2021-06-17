from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("film-detail/<int:pk>/", film_detail, name="film-detail"),
    path("create-film/", FilmCreate.as_view(), name="create-film"),
    path("film-detail/<int:pk>/update/", FilmUpdate.as_view(), name="update-film"),
    path("film-detail/<int:pk>/delete/", FilmDelete.as_view(), name="delete-film"),
]
