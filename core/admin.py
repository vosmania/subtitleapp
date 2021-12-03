from django.contrib import admin

# Register your models here.

from .models import MovieList, GenreChoices

admin.site.register(MovieList)
admin.site.register(GenreChoices)
