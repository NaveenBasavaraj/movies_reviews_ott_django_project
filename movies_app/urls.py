from django.urls import path, include
from movies_app.views import movies_list, movie_details, StreamerDetailAV, StreamAV

urlpatterns = [
    path("api/", include("movies_app.api.urls") ),
    path("list/", movies_list, name="movies-list"),
    path("list/<int:pk>/", movie_details, name="movies-details"),
    path("stream/list/", StreamAV.as_view(), name="stream-list"),
    path("stream/list/<int:pk>/", StreamerDetailAV.as_view(), name="stream-details"),
]