from django.test import TestCase
from .models import Artist, Painting

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

class PaintingModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            title='Vincent van Gogh',
            birth_date=1853,
            death_date=1890
        )
        self.painting = Painting.objects.create(
            title='Starry Night',
            width=92.1,
            height=73.7,
            depth=1.7,
            artist_id=self.artist
        )

    def test_str_representation(self):
        self.assertEqual(str(self.painting), 'Starry Night')

    def test_default_values(self):
        self.assertEqual(self.painting.width, 92.1)
        self.assertEqual(self.painting.height, 73.7)
        self.assertEqual(self.painting.depth, 1.7)
        self.assertEqual(self.painting.artist_id, self.artist)

    def test_artist_foreign_key(self):
        self.assertEqual(self.painting.artist_id, self.artist)