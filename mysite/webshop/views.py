import requests
from django.http import HttpResponse
from django.views import View
from .models import Artists


def index(request):
    return HttpResponse("Hello, world. You're at the webshop index.")

class ArtistsView(View):
    def get(self, request):
        api_url = "https://api.artic.edu/api/v1/artists"

        response = requests.get(api_url)
        data = response.json()

        for artist_data in data['artists']:
            title = artist_data['title']
            birth_date = artist_data['birth_date']
            death_date = artist_data['death_date']

            artist, created = Artists.objects.get_or_create(title=title)

            artist.birth_date = birth_date
            artist.death_date = death_date
            artist.save()

        return HttpResponse("Obiekty Artists zostały zaktualizowane.")