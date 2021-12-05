from django import forms

from .models import MovieList, Upload


class AddMovie(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = '__all__'


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('file',)
