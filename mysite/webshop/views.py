import requests
from django.http import HttpResponse
from django.views import View
from .models import Artists, Painting


def index(request):
    return HttpResponse("Hello, world. You're at the webshop index.")

class ArtistsView(View):
    def get(self, request):
        api_url = "https://api.artic.edu/api/v1/artists"

        response = requests.get(api_url)
        data = response.json()

        for artist_data in data['data']:
            title = artist_data['title']
            birth_date = artist_data['birth_date']
            death_date = artist_data['death_date']
            print(title)
            print(birth_date)
            print(death_date)

            artist, created = Artists.objects.get_or_create(title=title)

            artist.birth_date = birth_date
            artist.death_date = death_date
            artist.save()

        return HttpResponse("Obiekty Artists zostały zaktualizowane.")
    
class PaintingsView(View):
    def get(self, request):
        api_url = "https://api.artic.edu/api/v1/artworks"

        response = requests.get(api_url)
        data = response.json()

        for artworks_data in data['data']:
            title = artworks_data['title']
            width = artworks_data['dimensions_detail'][0]["width_cm"]
            height = artworks_data['dimensions_detail'][0]["height_cm"]
            depth = artworks_data['dimensions_detail'][0]["depth_cm"]
            artist_id = artworks_data['artist_id']

            artist, created = Painting.objects.get_or_create(title=title)

            artist.width = width
            artist.height = height
            artist.depth = depth
            artist.save()

        return HttpResponse("Obiekty Artworks zostały zaktualizowane.")