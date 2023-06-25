from django.db import models

class Artist(models.Model):
    title = models.CharField(max_length = 200)
    birth_date = models.IntegerField(default = 0, null=True)
    death_date = models.IntegerField(default = 0, null=True)
    def __str__(self) -> str:
        return self.title
   
class Painting(models.Model):
    title = models.CharField(max_length = 200)
    width = models.FloatField(default = 0)
    height = models.FloatField(default = 0)
    depth = models.FloatField(default = 0)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title