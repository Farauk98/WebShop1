from django import forms
from .models import Painting, Artist

class PaintingsForm(forms.ModelForm):
    artist = forms.ModelChoiceField(queryset=Artist.objects.all(), label='Artysta')

    class Meta:
        model = Painting
        fields = ['title', 'width', 'height', 'depth', 'artist']


class ArtistsForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ['title', 'birth_date', 'death_date']
