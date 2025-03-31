from django.urls import path, include
from movies_app.views import movies_list, movie_details, StreamerDetailAV, StreamAV, ReviewAV, ReviewDetailAV
from movies_app.app_views import index, movies

urlpatterns = [
    path("api/", include("movies_app.api.urls") ),
    path("list/", movies_list, name="movies-list"),
    path("list/<int:pk>/", movie_details, name="movies-details"),
    path("stream/list/", StreamAV.as_view(), name="stream-list"),
    path("stream/list/<int:pk>/", StreamerDetailAV.as_view(), name="stream-details"),
    path("review/list/", ReviewAV.as_view(), name="review-list"),
    path("review/list/<int:pk>/", ReviewDetailAV.as_view(), name="review-details"),
]