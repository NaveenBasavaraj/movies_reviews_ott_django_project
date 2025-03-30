from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, generics, viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

# strange imports
from django_filters.rest_framework import DjangoFilterBackend

# app specific imports
from movies_app.models import Movie, Streamer, Review
from movies_app.api.serializers import MovieModelSerializer, ReviewModelSerializer, StreamerModelSerializer

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewModelSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)

class ReviewDetail(generics.ListAPIView):
    serializer_class = ReviewModelSerializer
    queryset = Review.objects.all()



class MovieList(generics.ListAPIView):
    serializer_class = MovieModelSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Movie.objects.filter(review_user__username=username)

class MovieDetail(generics.ListAPIView):
    serializer_class = MovieModelSerializer
    queryset = Movie.objects.all()


class StreamerList(generics.ListAPIView):
    serializer_class = StreamerModelSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Movie.objects.filter(review_user__username=username)

class StreamerDetail(generics.ListAPIView):
    serializer_class = StreamerModelSerializer
    queryset = Movie.objects.all()
