from django.db import models
import re


class GenreChoices(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre


# Create your models here.

class MovieList(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.CharField(max_length=10)
    genre = models.ManyToManyField(GenreChoices)
    description = models.TextField(null=True, blank=True)
    imdb_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def genreclean(self):
        raw = str(self.genre.values())
        regex = re.compile("(?<=: ')(.*?)(?='})")
        clean = regex.findall(raw)
        cleaner = str(clean)[1:-1].replace("'", "")
        return cleaner