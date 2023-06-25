from django.test import TestCase
from .models import Artist

class ArtistModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            title='Vincent van Gogh',
            birth_date=1853,
            death_date=1890
        )

    def test_str_representation(self):
        self.assertEqual(str(self.artist), 'Vincent van Gogh')

    def test_birth_date_default_value(self):
        artist = Artist.objects.create(title='Pablo Picasso')
        self.assertEqual(artist.birth_date, 0)

    def test_death_date_default_value(self):
        artist = Artist.objects.create(title='Leonardo da Vinci')
        self.assertEqual(artist.death_date, 0)