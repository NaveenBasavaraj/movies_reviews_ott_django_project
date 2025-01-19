from django.shortcuts import render
from movies_app.models import Movie,Streamer, Review
from rest_framework.decorators import api_view # function based views
from rest_framework.views import APIView # class based views
from movies_app.serializers import MovieSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET','POST'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)