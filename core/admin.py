from django.contrib import admin

from .models import MovieList, GenreChoices

# Register your models here.

admin.site.register(MovieList)
admin.site.register(GenreChoices)
