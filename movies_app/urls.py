from django.urls import path, include
from movies_app.views import movies_list

urlpatterns = [
    path("api/", include("movies_app.api.urls") ),
    path("list/", movies_list, name="movies-list"),
]