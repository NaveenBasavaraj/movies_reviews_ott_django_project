from django.shortcuts import render, get_object_or_404, get_list_or_404
from movies_app.models import Movie, Streamer, Review
from rest_framework.decorators import api_view # function based views
from rest_framework.views import APIView # class based views
from movies_app.serializers import MovieSerializer, StreamerSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle


class ReviewAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ReviewDetailAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Streamer.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = Streamer.objects.get(pk=pk)
        serializer = StreamerSerializer(platform, 
                                              data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Streamer.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        platform = Streamer.objects.all()
        serializer = StreamerSerializer(platform, 
                                        many=True, 
                                        context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamerDetailAV(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            platform = Streamer.objects.get(pk=pk)
        except Streamer.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamerSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = Streamer.objects.get(pk=pk)
        serializer = StreamerSerializer(platform, 
                                              data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Streamer.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        