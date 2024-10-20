from django.shortcuts import render
from watchbuddy.models import MoviesList, OttPlatform, UserReview
from django.http import JsonResponse


def movie_list(request):
    movies = MoviesList.objects.all()
    data = {
        'movies': list(movies.values())
        }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = MoviesList.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }
    return JsonResponse(data)

def ott_list(request):
    otts = OttPlatform.objects.all()
    data = {
        'otts': list(otts.values())
        }
    return JsonResponse(data)


def ott_details(request, pk):
    ott = OttPlatform.objects.get(pk=pk)
    data = {
        'name': ott.name,
        'about': ott.about,
        'website': ott.website
    }
    return JsonResponse(data)