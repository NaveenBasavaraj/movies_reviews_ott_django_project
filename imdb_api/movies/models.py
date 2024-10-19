from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class SteamingPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    allows_multi_users = models.BooleanField(default=False)
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)
    platform = models.ForeignKey(SteamingPlatform, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    description = models.CharField(max_length=100)
    review = models.TextField()
    is_active = models.BooleanField(default=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating * '*')