from rest_framework import serializers
from watchbuddy.models import MoviesList, OttPlatform, UserReview

class UserReviewSerializer(serializers.ModelSerializer):
    review = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserReview
        fields ="__all__"

class MovieListSerializer(serializers.ModelSerializer):
    userreview = UserReviewSerializer(many=True, read_only=True)
    ottplatform = serializers.CharField(source='ottplatform.name')

    class Meta:
        model = MoviesList
        fields = "__all__"

class OttPlatformSerializer(serializers.ModelSerializer):
    movielist = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = OttPlatform
        fields = "__all__"