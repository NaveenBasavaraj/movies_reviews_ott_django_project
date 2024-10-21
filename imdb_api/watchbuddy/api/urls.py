from django.urls import path
from watchbuddy.api.views import MovieListAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='MovieListAV'),
]
