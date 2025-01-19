from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Streamer(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE, related_name="movie")
    is_active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    create_ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    is_active = models.BooleanField(default=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " | " + self.movie.title + " | " + str(self.review_user)