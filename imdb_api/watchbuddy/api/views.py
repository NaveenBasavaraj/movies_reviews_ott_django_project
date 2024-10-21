from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status, filters
# class based views
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
# function based views
from rest_framework.decorators import api_view
# permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# throttling
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
# from django_filters.rest_framework import DjangoFilterBackend
# models
from watchbuddy.models import MoviesList, UserReview, OttPlatform
# serializers
from watchbuddy.api.serializers import UserReviewSerializer, MovieListSerializer, OttPlatformSerializer


class MovieListAV(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        movies = MoviesList.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)