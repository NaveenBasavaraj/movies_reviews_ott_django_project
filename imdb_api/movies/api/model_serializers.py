from movies.models import Movie, SteamingPlatform, Review
from rest_framework.serializers import ModelSerializer

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class StreamSerializer(ModelSerializer):
    class Meta:
        model = SteamingPlatform
        fields = "__all__"


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"