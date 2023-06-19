from django import forms
from .models import Painting, Artists

class PaintingsForm(forms.ModelForm):
    artist = forms.ModelChoiceField(queryset=Artists.objects.all(), label='Artysta')

    class Meta:
        model = Painting
        fields = ['title', 'width', 'height', 'depth', 'artist']


class ArtistsForm(forms.ModelForm):

    class Meta:
        model = Artists
        fields = ['title', 'birth_date', 'death_date']
