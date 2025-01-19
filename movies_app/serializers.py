from rest_framework import serializers
from movies_app.models import Movie, Streamer, Review
from django.contrib.auth.models import User

class StreamerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # The ID of the Streamer, read-only
    name = serializers.CharField(max_length=30)  # Streamer name
    about = serializers.CharField(max_length=150)  # Streamer description or about
    website = serializers.URLField(max_length=100)  # Streamer's website URL

    def create(self, validated_data):
        # Create a new Streamer instance
        return Streamer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update existing Streamer instance
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance


# Review Serializer
class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    review_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Link to the User model
    rating = serializers.IntegerField(min_value=1, max_value=5)  # Rating between 1 and 5
    description = serializers.CharField(max_length=200, required=False)  # Optional description
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())  # Link to the Movie model
    is_active = serializers.BooleanField(default=True)
    create_ts = serializers.DateTimeField(read_only=True)
    update_ts = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        # Ensure rating is within valid range (1-5), though the IntegerField already limits this
        if data['rating'] < 1 or data['rating'] > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return data

    def create(self, validated_data):
        # Create a new review instance
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update review fields
        instance.review_user = validated_data.get('review_user', instance.review_user)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.description = validated_data.get('description', instance.description)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance



# Custom validation function
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Title is too short!")
    return value

# Movie Serializer
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(validators=[name_length])
    storyline = serializers.CharField()
    is_active = serializers.BooleanField()
    streamer_id = serializers.IntegerField()  # This will represent the Streamer ID (as a foreign key)
    avg_rating = serializers.FloatField(read_only=True)
    number_rating = serializers.IntegerField(read_only=True)
    create_ts = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError("Title and Storyline should be different!")
        return data

    def create(self, validated_data):
        # Assuming streamer_id is passed in the data to create the movie
        streamer_id = validated_data.pop('streamer_id')  # Remove streamer_id to handle separately
        movie = Movie.objects.create(streamer_id=streamer_id, **validated_data)
        return movie

    def update(self, instance, validated_data):
        # Update movie details
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        
        # Update the streamer_id if passed in the update request
        if 'streamer_id' in validated_data:
            instance.streamer_id = validated_data['streamer_id']
        
        instance.save()
        return instance