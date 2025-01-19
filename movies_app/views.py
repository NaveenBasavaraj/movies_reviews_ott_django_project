from django.shortcuts import render, get_object_or_404, get_list_or_404
from movies_app.models import Movie,Streamer, Review
from rest_framework.decorators import api_view # function based views
from rest_framework.views import APIView # class based views
from movies_app.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def movies_list(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        if movie:
            movie.delete({"message":f"deleted {movie}"}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        