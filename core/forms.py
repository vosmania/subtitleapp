from django.forms import ModelForm
from .models import MovieList



class AddMovie(ModelForm):
    class Meta:
        model = MovieList
        fields = '__all__'
