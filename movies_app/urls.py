from django.urls import path, include
from movies_app.views import movies_list, movie_details

urlpatterns = [
    path("api/", include("movies_app.api.urls") ),
    path("list/", movies_list, name="movies-list"),
    path("list/<int:pk>/", movie_details, name="movies-details"),
]