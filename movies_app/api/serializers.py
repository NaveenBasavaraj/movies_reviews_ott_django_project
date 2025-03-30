from rest_framework import serializers
from movies_app.models import Movie, Streamer, Review

class ReviewModelSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('movie',)
        # fields = "__all__"


class MovieModelSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = Movie
        fields = "__all__"


class StreamerModelSerializer(serializers.ModelSerializer):
    watchlist = MovieModelSerializer(many=True, read_only=True)

    class Meta:
        model = Streamer
        fields = "__all__"