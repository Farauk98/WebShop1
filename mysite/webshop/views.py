import requests
from django.http import HttpResponse
from django.views import View
from .models import Artist, Painting
from .forms import PaintingsForm, ArtistsForm
from django.shortcuts import render, redirect, get_object_or_404

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

            artist, created = Artist.objects.get_or_create(title=title)

            artist.birth_date = birth_date
            artist.death_date = death_date
            artist.save()

        return HttpResponse("Obiekty Artists zostały zaktualizowane.")
    
class ArtistsCreateView(View):   
    def get(self, request):
        form = ArtistsForm()
        context = {
            'form': form,
        }
        return render(request, "form.html", context)

    def post(self, request):
        form = ArtistsForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return HttpResponse("Obiekty Artists zostały dodane.")
        context = {
            'form': form,
        }
        return render(request, "form.html", context)
    
class ArtistSelectView(View):
    def get(self, request):
        artists = Artist.objects.all()
        context = {
            'objects': artists,
            'object_type': 'artists'
        }
        return render(request, 'select.html', context)

    def post(self, request):
        artist_id = request.POST.get('object_id')
        if artist_id:
            return redirect('delete-object', object_type='artists', object_id=artist_id)
        else:
            return HttpResponse("Nie wybrano żadnego artysty.")
    
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

class PaintingsCreateView(View):   
    def get(self, request):
        form = PaintingsForm()
        context = {
            'form': form,
        }
        return render(request, "form.html", context)

    def post(self, request):
        form = PaintingsForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
            return HttpResponse("Obiekty Paintings zostały dodane.")
        context = {
            'form': form,
        }
        return render(request, "form.html", context)

class PaintingSelectView(View):
    def get(self, request):
        paintings = Painting.objects.all()
        context = {
            'objects': paintings,
            'object_type': 'paintings'
        }
        return render(request, 'select.html', context)

    def post(self, request):
        painting_id = request.POST.get('object_id')
        if painting_id:
            return redirect('delete-object', object_type='paintings', object_id=painting_id)
        else:
            return HttpResponse("Nie wybrano żadnego obrazu.")

class ObjectDeleteView(View):
    def get(self, request,object_type, object_id):
        if object_type =='paintings':
            object = get_object_or_404(Painting, id=object_id)
        elif object_type =='artists':
            object = get_object_or_404(Artist, id=object_id)
        object.delete()
        return HttpResponse(f"Obiekt {object_type.capitalize()} został usunięty.")
        
        
