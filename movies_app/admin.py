from django.contrib import admin
from movies_app.models import Movie, Streamer, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Streamer)
admin.site.register(Review)