from django.db import models
from django.utils import timezone

# Create your models here.
# sncy: by inherit Model class, Genre will also all the needed functionality


class Genre(models.Model):
    # sncy: name is attribute
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # sncy: each Movie needs to be associated with a genre
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
