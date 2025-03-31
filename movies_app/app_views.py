from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    """Render the home page."""
    return render(request, 'movies_app/index.html')

def movies(request):
    """Render the movies list page with data from the Movie model."""
    movies = Movie.objects.all()  # Fetch all movies from the database
    context = {'movies': movies}
    return render(request, 'movies_app/movies.html', context)